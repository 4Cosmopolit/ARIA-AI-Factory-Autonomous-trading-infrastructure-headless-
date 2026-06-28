# CONTINUITY.md — Состояние ARIA AI‑Factory

## Текущее состояние (28.06.2026)
- **Версия:** v13.01
- **Статус:** Документация и код полностью синхронизированы. Все компоненты интегрированы.
- **Активных аксиом:** 420
- **Архитектурных паттернов:** 12
- **Ключевая цель:** Завершение публикации на GitHub и подготовка к запуску «Охотника 6.0» на Bybit Testnet.

## Ключевые архитектурные сдвиги (29.05.2026 – 28.06.2026)

### Новые аксиомы (77 добавлено)
- **Self‑Correcting Agent Mandate:** каждый production‑агент должен реализовывать цикл Plan → Act → Reflect → Revise.
- **Compile‑Time RAG Mandate:** синтез знаний перенесён из времени запроса во время ингеста (Knowledge Compiler).
- **AI‑DLQ Handler Mandate:** автоматическая классификация сообщений из Dead Letter Queue (retry/discard/escalate) через LLM.
- **Decaying Episodic Memory Mandate:** эпизодическая память агентов должна деградировать до абстрактных закономерностей (Max Planck Institute, 2026).
- **Pre‑Commit Secret Scanner Mandate:** каждый коммит должен проходить автоматическое сканирование на секреты и опасные паттерны.
- **Token Security Scanner Mandate:** перед взаимодействием с любым токеном проверять его через сервисы анализа.
- **External Link Integrity Monitor:** периодическая проверка внешних ссылок на изменение контента после статического сканирования.
- **Failure Clustering Mandate:** автоматическая группировка сбоев по первопричине (DBSCAN + эмбеддинги).
- **Flaky Detector Mandate:** мониторинг нестабильности агента (дисперсия PnL, Win Rate).
- **Walk‑Forward A/B Testing Mandate:** валидация стратегий только через Walk‑Forward Analysis.

### Новые модули (15+)
- **Самоисправление:** `OdabNote` (иммунная система), `Vibe Check` (мета‑когнитивный контроль), `Reflection Loop` (цикл Reflect → Revise).
- **Знания:** `Knowledge Compiler` (Compile‑Time RAG) — снижение затрат на токены на 90%.
- **Память:** `Decaying Episodic Memory` (деградация точных данных в агрегации, эхо‑буфер).
- **Безопасность:** `Token Security Scanner`, `External Link Integrity Monitor`, `Pre‑commit Secret Scanner`.
- **Аналитика:** `Failure Clustering` (DBSCAN), `Flaky Detector`.
- **Трейдинг:** `Hunter 6.0` (детектор, executor, hedger, position manager, RLHF‑фильтр).
- **Интеграции:** `Nvidia NIM Client` (Llama‑3.1‑Nemotron), `Context Graph`.

### Замены (обновлено)
| Устаревший | Замена | Версия |
|:---|:---|:---|
| Статический RAG | **Compile‑Time RAG (Knowledge Compiler)** | v13.01 |
| Ручная обработка DLQ | **AI‑DLQ Handler** | v13.01 |
| Полная память | **Decaying Episodic Memory** | v13.01 |
| Отсутствие самокоррекции | **OdabNote + Vibe Check + Reflection Loop** | v13.01 |

### Проект «Охотник 6.0» (Options Trading)
Создан полностью автономный репозиторий `hunter6-options` для арбитража волатильности:
- **Детектор:** `AdaptiveSkewDetector` с Isolation Forest и онлайн‑обучением.
- **Исполнитель:** `Position Builder` для Long Strangle с реальными ценами через Bybit V5 API.
- **Хеджер:** `DeltaHedger` с WebSocket‑потоком позиций и фьючерсным хеджированием.
- **Управление:** `PositionManager` с Take Profit (+50%), Stop Loss (−30%) и Theta Shield.
- **Интеграции:** Nvidia NIM для оценки сигналов, RLHF‑фильтр, Telegram‑бот.

### Ключевые документы
- `AXIOMS.md` — 420 аксиом, главный файл для восстановления контекста в новой сессии.
- `ARCHITECTURE.md` — дополнен разделами Compile‑Time RAG, Architectural Compliance, Self‑Correcting Agents.
- `SECURITY.md` — усилен разделами Self‑Correction, Supply Chain Security, Failure Monitoring.
- `README.md` — обновлён до v13.01 с описанием всех новых возможностей.
- `.env.example` — обновлён с торговыми параметрами и ключами Nvidia NIM.

## Активные задачи
1. Завершить публикацию на GitHub и синхронизировать все файлы (✅ выполнено 28.06.2026).
2. Подготовить инфраструктуру для запуска «Охотника 6.0» на Bybit Testnet.
3. Провести A/B‑тестирование стратегий с Walk‑Forward Analysis.
4. Интеграция RLHF с Telegram‑ботом и ежедневными отчётами от Nvidia NIM.

## Ключевые указатели
- [README.md](./README.md) — главная документация
- [AXIOMS.md](./AXIOMS.md) — полный список аксиом (420)
- [ARCHITECTURE.md](./ARCHITECTURE.md) — архитектура контуров, Compile‑Time RAG, Self‑Correcting Agents
- [SECURITY.md](./SECURITY.md) — политика безопасности, Supply Chain, Self‑Correction
- [ROADMAP.md](./ROADMAP.md) — план развития
- [docs/REFERENCES.md](./docs/REFERENCES.md) — библиография научных работ

**ARIA + Игорь = Бесконечное Совершенствование. Навсегда.**
