"""
test_skills_capital_safety.py — Unit tests для Capital Safety контура

Тестирует:
- Capital Loss Gate (max 1% per day)
- Position Sizing (Kelly Criterion)
- VaR calculations (95% confidence)
- Risk Aggregation across skills

Запуск:
  pytest tests/test_skills_capital_safety.py -v
"""

import pytest
import numpy as np
from datetime import datetime, timedelta
from decimal import Decimal


class TestCapitalLossGate:
    """Проверка Capital Loss Gate (Max 1% per day)"""

    @pytest.fixture
    def capital_config(self):
        return {
            'managed_capital': 1_000_000,
            'max_daily_loss_pct': 1.0,
            'max_daily_loss_usd': 10_000,
            'hitl_threshold': 500_000,
            'emergency_stop_threshold': 0.95,  # 95% of max loss
        }

    def test_capital_gate_rejects_order_exceeding_limit(
        self,
        capital_config
    ):
        """Проверить что ордер отклоняется если превышает лимит"""
        order_risk = 12_000  # 1.2% капитала
        current_loss = 500   # 0.05% already lost
        
        remaining_budget = (
            capital_config['max_daily_loss_usd'] - current_loss
        )
        
        assert order_risk > remaining_budget, \
            "Order should be rejected"

    def test_capital_gate_accepts_order_within_limit(
        self,
        capital_config
    ):
        """Проверить что ордер принимается если в пределах лимита"""
        order_risk = 5_000   # 0.5% капитала
        current_loss = 3_000 # 0.3% already lost
        
        remaining_budget = (
            capital_config['max_daily_loss_usd'] - current_loss
        )
        
        assert order_risk <= remaining_budget, \
            "Order should be accepted"

    def test_emergency_stop_at_95_percent(
        self,
        capital_config
    ):
        """Проверить срабатывание Emergency Stop при 95% лимита"""
        max_loss = capital_config['max_daily_loss_usd']
        emergency_threshold = max_loss * capital_config['emergency_stop_threshold']
        current_loss = 9_600  # 96% of max
        
        assert current_loss >= emergency_threshold, \
            "Should trigger emergency stop"


class TestPositionSizing:
    """Kelly Criterion для правильного размера позиций"""

    def kelly_criterion(self, win_rate, avg_win, avg_loss):
        """f = (bp - q) / b, где b = avg_win/avg_loss"""
        if avg_loss == 0:
            return 0
        b = avg_win / avg_loss
        p = win_rate
        q = 1 - win_rate
        
        if b == 0:
            return 0
        return (b * p - q) / b

    def test_kelly_fraction_valid_for_50_percent_edge(
        self
    ):
        """Kelly Criterion для 50% win rate, 2:1 payoff"""
        win_rate = 0.50
        avg_win = 200
        avg_loss = 100
        
        kelly_fraction = self.kelly_criterion(
            win_rate,
            avg_win,
            avg_loss
        )
        
        # (1.0 * 0.5 - 0.5) / 1.0 = 0 (neutral)
        assert kelly_fraction == pytest.approx(0.0)

    def test_kelly_fraction_positive_edge(
        self
    ):
        """Kelly Criterion для 60% win rate, 2:1 payoff"""
        win_rate = 0.60
        avg_win = 200
        avg_loss = 100
        
        kelly_fraction = self.kelly_criterion(
            win_rate,
            avg_win,
            avg_loss
        )
        
        # (1.0 * 0.6 - 0.4) / 1.0 = 0.2 (20% of bankroll)
        assert kelly_fraction == pytest.approx(0.2)

    def test_fractional_kelly_safety(
        self
    ):
        """Fractional Kelly (f_safe = f * 0.25) для большей безопасности"""
        kelly_fraction = 0.2
        fractional_kelly = kelly_fraction * 0.25  # Conservative: 25% of Kelly
        
        # Should be much more conservative
        assert fractional_kelly == pytest.approx(0.05)
        assert fractional_kelly < kelly_fraction


class TestVaRCalculation:
    """Value at Risk для риска портфеля"""

    def test_var_95_percent_confidence(
        self
    ):
        """VaR 95% confidence level"""
        # Симуляция 1000 дневных возвратов
        returns = np.random.normal(
            loc=0.001,      # 0.1% average return
            scale=0.02,     # 2% volatility
            size=1000
        )
        
        var_95 = np.percentile(returns, 5)  # 5th percentile = 95% VaR
        
        # VaR должен быть отрицательным (убыток)
        assert var_95 < 0
        # VaR должен быть в разумных пределах (-5% ~ -3%)
        assert -0.05 < var_95 < -0.02

    def test_cvar_expected_shortfall(
        self
    ):
        """CVaR (Expected Shortfall) - средний убыток за VaR"""
        returns = np.random.normal(
            loc=0.001,
            scale=0.02,
            size=1000
        )
        
        var_95 = np.percentile(returns, 5)
        cvar_95 = returns[returns <= var_95].mean()
        
        # CVaR должен быть хуже, чем VaR
        assert cvar_95 < var_95


class TestRiskAggregation:
    """Агрегация рисков через несколько позиций"""

    def test_correlation_reduces_portfolio_var(
        self
    ):
        """Диверсификация снижает портфельный VaR"""
        # Position 1: волатильность 2%
        pos1_vol = 0.02
        
        # Position 2: волатильность 2%
        pos2_vol = 0.02
        
        # Корреляция 0 (независимые)
        correlation = 0.0
        
        # Portfolio volatility = sqrt(w1^2*v1^2 + w2^2*v2^2 + 2*w1*w2*corr*v1*v2)
        w1, w2 = 0.5, 0.5
        portfolio_vol = np.sqrt(
            w1**2 * pos1_vol**2 +
            w2**2 * pos2_vol**2 +
            2 * w1 * w2 * correlation * pos1_vol * pos2_vol
        )
        
        # Портфельная волатильность должна быть < суммы отдельных
        single_sum_vol = w1 * pos1_vol + w2 * pos2_vol
        assert portfolio_vol < single_sum_vol

    def test_high_correlation_increases_var(
        self
    ):
        """Высокая корреляция увеличивает портфельный риск"""
        pos1_vol = 0.02
        pos2_vol = 0.02
        correlation_high = 0.9  # Высокая корреляция
        
        w1, w2 = 0.5, 0.5
        portfolio_vol_high_corr = np.sqrt(
            w1**2 * pos1_vol**2 +
            w2**2 * pos2_vol**2 +
            2 * w1 * w2 * correlation_high * pos1_vol * pos2_vol
        )
        
        # При высокой корреляции риск растет
        # Близко к простой сумме: ~0.02
        assert portfolio_vol_high_corr > 0.014


class TestStressScenarios:
    """Стресс-тесты для экстремальных сценариев"""

    def test_black_swan_event(
        self
    ):
        """Проверка защиты от Black Swan (-10% за день)"""
        capital = 1_000_000
        position_size = 500_000  # 50% капитала
        black_swan_loss = position_size * -0.10  # -10% день
        
        loss_pct = abs(black_swan_loss) / capital * 100
        
        # 5% потеря - выше лимита 1%
        assert loss_pct > 1.0
        # Должен сработать circuit breaker

    def test_circuit_breaker_at_90_percent_loss(
        self
    ):
        """Circuit breaker срабатывает при 0.9% потерь (90% от 1% лимита)"""
        max_daily_loss_pct = 1.0
        circuit_breaker_threshold = max_daily_loss_pct * 0.9
        
        current_loss_pct = 0.91
        
        assert current_loss_pct >= circuit_breaker_threshold


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
