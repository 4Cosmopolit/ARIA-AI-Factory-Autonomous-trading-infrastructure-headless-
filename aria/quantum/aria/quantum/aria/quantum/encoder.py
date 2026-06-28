#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Запуск квантового детектора аномалий на финансовых данных.

Использование:
    python -m aria.quantum.run --config configs/quantum/domain_volatility.yaml
    python -m aria.quantum.run --config configs/quantum/base.yaml --synthetic
    python -m aria.quantum.run --config ... --plot
"""

import argparse
import logging
import sys
import yaml
import json
from pathlib import Path
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score

# Добавляем путь к проекту (если запуск из корня)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aria.quantum import AnomalyEngine, FinancialDomainAdapter
from aria.quantum.encoder import PCAEncoder
from aria.quantum.scorer import QuantumSVM

# Импортируем классические бейзлайны
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.neural_network import MLPRegressor  # для AE reconstruction

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("quantum_run")


def load_data_from_alpha_vantage(symbol: str = "BTCUSD", api_key: str = None,
                                 outputsize: str = "full") -> pd.DataFrame:
    """Загружает дневные OHLCV данные через Alpha Vantage."""
    try:
        import requests
    except ImportError:
        raise ImportError("Установите requests: pip install requests")
    
    if api_key is None:
        logger.warning("Alpha Vantage API ключ не указан. Использую демо-ключ (может быть ограничен).")
        api_key = "demo"  # ограниченный ключ
    
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": symbol,
        "market": "USD",
        "apikey": api_key,
        "outputsize": outputsize,
        "datatype": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "Time Series (Digital Currency Daily)" not in data:
        logger.error(f"Ошибка загрузки: {data.get('Note', data)}")
        return None
    
    ts = data["Time Series (Digital Currency Daily)"]
    df = pd.DataFrame.from_dict(ts, orient="index")
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    # Переименовываем колонки
    df = df.rename(columns={
        "1a. open (USD)": "open",
        "2a. high (USD)": "high",
        "3a. low (USD)": "low",
        "4a. close (USD)": "close",
        "5. volume": "volume"
    })
    df = df.astype(float)
    return df


def load_synthetic_data(n_samples: int = 5000, n_features: int = 10, anomaly_ratio: float = 0.05,
                        seed: int = 42) -> pd.DataFrame:
    """Генерирует синтетические данные для тестирования."""
    np.random.seed(seed)
    # Нормальное распределение (рыночные условия)
    X = np.random.randn(n_samples, n_features)
    # Добавляем аномалии (сдвиг или масштаб)
    n_anomalies = int(anomaly_ratio * n_samples)
    if n_anomalies > 0:
        anomaly_idx = np.random.choice(n_samples, n_anomalies, replace=False)
        X[anomaly_idx] += np.random.normal(loc=3, scale=2, size=(n_anomalies, n_features))
    # Создаём DataFrame с произвольными названиями признаков
    columns = [f"feat_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=columns)
    # Добавляем столбец 'close' (для совместимости с адаптером можно)
    df['close'] = X[:, 0].cumsum() + 100  # имитация цены
    df['open'] = df['close'].shift(1).fillna(100)
    df['high'] = df[['open', 'close']].max(axis=1) + 0.5
    df['low'] = df[['open', 'close']].min(axis=1) - 0.5
    df['volume'] = np.abs(X[:, 1]) * 1000
    return df


def prepare_data(df: pd.DataFrame, config: dict) -> tuple:
    """
    Подготавливает данные: извлекает признаки, разделяет на train/test.
    Возвращает (X_train, y_train, X_test, y_test, feature_names)
    """
    adapter = FinancialDomainAdapter(lookback=config['domain'].get('lookback', 30))
    # Если в df нет нужных колонок, но есть только признаки, то используем их напрямую
    # Проверяем наличие OHLCV
    required = ['open', 'high', 'low', 'close', 'volume']
    if all(col in df.columns for col in required):
        X = adapter.ingest(df)
    else:
        # если нет, используем все числовые колонки как признаки
        logger.warning("Нет OHLCV-колонок, использую все числовые признаки.")
        X = df.select_dtypes(include=[np.number]).values
    
    # Разделение с учётом аномалий (если есть y)
    if 'y' in df.columns:
        y = df['y'].values
        # Простое разделение по времени (первые 70% train)
        n_train = int(0.7 * len(X))
        X_train, y_train = X[:n_train], y[:n_train]
        X_test, y_test = X[n_train:], y[n_train:]
    else:
        # Используем встроенный split из адаптера (с искусственными аномалиями)
        X_train, y_train, X_test, y_test = adapter.split(X, anomaly_ratio=config['domain'].get('anomaly_ratio', 0.05))
    
    return X_train, y_train, X_test, y_test


def train_classical_baselines(X_train, X_test, y_test, config: dict) -> dict:
    """Обучает классические модели и возвращает метрики."""
    baselines = {}
    # 1. One-Class SVM с RBF ядром
    svm = OneClassSVM(nu=config['quantum']['nu'], kernel='rbf', gamma='scale')
    svm.fit(X_train)
    y_pred_svm = svm.predict(X_test)
    # Преобразуем метки в 1/-1
    y_true = np.where(y_test == 1, 1, -1)
    metrics = {
        'auc': roc_auc_score((y_true == -1).astype(int), -svm.score_samples(X_test)),
        'accuracy': accuracy_score(y_true, y_pred_svm),
        'f1': f1_score(y_true, y_pred_svm, pos_label=-1)
    }
    baselines['OneClassSVM'] = metrics
    
    # 2. Isolation Forest
    iso = IsolationForest(contamination=config['domain'].get('anomaly_ratio', 0.05), random_state=42)
    iso.fit(X_train)
    y_pred_iso = iso.predict(X_test)
    metrics_iso = {
        'auc': roc_auc_score((y_true == -1).astype(int), -iso.score_samples(X_test)),
        'accuracy': accuracy_score(y_true, y_pred_iso),
        'f1': f1_score(y_true, y_pred_iso, pos_label=-1)
    }
    baselines['IsolationForest'] = metrics_iso
    
    # 3. Autoencoder reconstruction error (если есть достаточно данных)
    try:
        from sklearn.decomposition import PCA
        # Используем PCA как простую реконструкцию
        pca = PCA(n_components=0.8)  # объяснённая дисперсия 80%
        pca.fit(X_train)
        X_recon = pca.inverse_transform(pca.transform(X_test))
        recon_error = np.mean((X_test - X_recon) ** 2, axis=1)
        # Порог по квантилю на обучающих данных
        train_recon = np.mean((X_train - pca.inverse_transform(pca.transform(X_train))) ** 2, axis=1)
        threshold = np.percentile(train_recon, 95)
        y_pred_recon = np.where(recon_error > threshold, -1, 1)
        # AUC по recon_error (чем больше ошибка, тем более аномально)
        auc_recon = roc_auc_score((y_true == -1).astype(int), recon_error)
        metrics_recon = {
            'auc': auc_recon,
            'accuracy': accuracy_score(y_true, y_pred_recon),
            'f1': f1_score(y_true, y_pred_recon, pos_label=-1)
        }
        baselines['PCA_Recon'] = metrics_recon
    except Exception as e:
        logger.warning(f"PCA reconstruction не удался: {e}")
    
    return baselines


def main():
    parser = argparse.ArgumentParser(description="Запуск квантового детектора аномалий")
    parser.add_argument("--config", required=True, help="Путь к YAML конфигу")
    parser.add_argument("--synthetic", action="store_true", help="Генерировать синтетические данные вместо загрузки")
    parser.add_argument("--plot", action="store_true", help="Построить графики результатов")
    parser.add_argument("--output", type=str, default="runs/quantum/result.json", help="Путь для сохранения результатов")
    args = parser.parse_args()
    
    # Загрузка конфига
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Создаём директорию для выходных данных
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 1. Загрузка данных
    if args.synthetic:
        logger.info("Использую синтетические данные")
        df = load_synthetic_data(n_samples=5000, anomaly_ratio=config['domain'].get('anomaly_ratio', 0.05))
    else:
        # Попытка загрузки реальных данных (Alpha Vantage)
        api_key = os.getenv("ALPHA_VANTAGE_KEY", "demo")
        df = load_data_from_alpha_vantage(symbol="BTCUSD", api_key=api_key)
        if df is None:
            logger.warning("Не удалось загрузить данные. Использую синтетические.")
            df = load_synthetic_data(n_samples=2000)
    
    # 2. Подготовка данных
    X_train, y_train, X_test, y_test = prepare_data(df, config)
    logger.info(f"Train: {X_train.shape}, Test: {X_test.shape}, аномалий в тесте: {np.sum(y_test == -1)}")
    
    # 3. Квантовый детектор
    logger.info("Инициализация квантового движка...")
    engine = AnomalyEngine(config)
    
    # Обучение
    start_time = datetime.now()
    engine.fit(X_train)
    train_time = (datetime.now() - start_time).total_seconds()
    logger.info(f"Квантовое обучение завершено за {train_time:.2f} сек")
    
    # Прогноз
    y_pred_q = engine.predict(X_test)
    scores_q = engine.score_samples(X_test)
    
    # Метрики квантового
    y_true = np.where(y_test == 1, 1, -1)
    auc_q = roc_auc_score((y_true == -1).astype(int), -scores_q)
    acc_q = accuracy_score(y_true, y_pred_q)
    f1_q = f1_score(y_true, y_pred_q, pos_label=-1)
    
    quantum_metrics = {
        'auc': auc_q,
        'accuracy': acc_q,
        'f1': f1_q,
        'train_time': train_time,
        'n_qubits': config['quantum']['n_qubits'],
        'feature_map': config['quantum']['feature_map'],
        'reps': config['quantum']['reps']
    }
    logger.info(f"Квантовый AUC: {auc_q:.4f}, Accuracy: {acc_q:.4f}, F1: {f1_q:.4f}")
    
    # 4. Классические бейзлайны
    logger.info("Обучение классических бейзлайнов...")
    baseline_metrics = train_classical_baselines(X_train, X_test, y_test, config)
    
    # 5. Сравнение и вывод
    results = {
        'quantum': quantum_metrics,
        'baselines': baseline_metrics,
        'config': config,
        'data_info': {
            'train_samples': X_train.shape[0],
            'test_samples': X_test.shape[0],
            'anomalies_test': int(np.sum(y_test == -1)),
            'features': X_train.shape[1]
        }
    }
    
    # Сохранение результатов
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    logger.info(f"Результаты сохранены в {output_path}")
    
    # 6. Построение графиков (опционально)
    if args.plot:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        # Распределение scores
        axes[0].hist(scores_q[y_true == 1], bins=30, alpha=0.5, label='Normal')
        axes[0].hist(scores_q[y_true == -1], bins=30, alpha=0.5, label='Anomaly')
        axes[0].set_title('Квантовые anomaly scores')
        axes[0].legend()
        # ROC кривая
        from sklearn.metrics import roc_curve
        fpr, tpr, _ = roc_curve((y_true == -1).astype(int), -scores_q)
        axes[1].plot(fpr, tpr, label=f'Quantum (AUC={auc_q:.3f})')
        # Добавим бейзлайны
        for name, m in baseline_metrics.items():
            # Для простоты рисуем только если есть AUC
            if 'auc' in m:
                # Приблизительно
                axes[1].plot([0, 1], [0, 1], 'k--', alpha=0.3)
        axes[1].set_xlabel('FPR')
        axes[1].set_ylabel('TPR')
        axes[1].set_title('ROC Curves')
        axes[1].legend()
        plt.tight_layout()
        plot_path = output_path.parent / f"roc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(plot_path)
        logger.info(f"График сохранён в {plot_path}")
        plt.show()
    
    # 7. Вывод summary
    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ")
    print("="*60)
    print(f"Квантовый: AUC={auc_q:.4f}, Acc={acc_q:.4f}, F1={f1_q:.4f} (время {train_time:.1f}с)")
    for name, m in baseline_metrics.items():
        print(f"{name}: AUC={m.get('auc',0):.4f}, Acc={m.get('accuracy',0):.4f}, F1={m.get('f1',0):.4f}")
    print("="*60)
    
    # 8. Сохраняем также для лога
    log_path = output_path.parent / "run_log.txt"
    with open(log_path, 'w') as f:
        f.write(f"Запуск: {datetime.now()}\n")
        f.write(f"Конфиг: {args.config}\n")
        f.write(f"Квантовый: {quantum_metrics}\n")
        f.write("Бейзлайны:\n")
        for name, m in baseline_metrics.items():
            f.write(f"  {name}: {m}\n")
    logger.info(f"Лог сохранён в {log_path}")

if __name__ == "__main__":
    import os
    main()
