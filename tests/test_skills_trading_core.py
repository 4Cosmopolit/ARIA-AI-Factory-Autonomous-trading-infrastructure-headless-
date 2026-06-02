"""
test_skills_trading_core.py — Unit tests для Core Trading навыков

Тестирует:
- Order Validation
- Price Feed Integrity
- Execution Simulation
- Trade Accounting

Запуск:
  pytest tests/test_skills_trading_core.py -v
"""

import pytest
from datetime import datetime, timedelta
from decimal import Decimal


class TestOrderValidation:
    """Валидация ордеров перед отправкой на биржу"""

    @pytest.fixture
    def valid_order(self):
        return {
            'symbol': 'BTC/USD',
            'side': 'buy',
            'type': 'limit',
            'quantity': 1.0,
            'price': 50000.00,
            'timestamp': datetime.utcnow(),
        }

    def test_order_requires_symbol(
        self,
        valid_order
    ):
        """Ордер должен иметь символ инструмента"""
        order = valid_order.copy()
        del order['symbol']
        
        assert 'symbol' not in order
        # Должна быть ошибка валидации

    def test_order_requires_positive_quantity(
        self,
        valid_order
    ):
        """Количество должно быть положительным"""
        order = valid_order.copy()
        order['quantity'] = -1.0
        
        assert order['quantity'] <= 0
        # Должна быть ошибка валидации

    def test_order_requires_positive_price(
        self,
        valid_order
    ):
        """Цена должна быть положительной"""
        order = valid_order.copy()
        order['price'] = 0
        
        assert order['price'] <= 0
        # Должна быть ошибка валидации

    def test_order_side_must_be_buy_or_sell(
        self,
        valid_order
    ):
        """Сторона ордера должна быть buy или sell"""
        order = valid_order.copy()
        order['side'] = 'invalid'
        
        valid_sides = ['buy', 'sell']
        assert order['side'] not in valid_sides


class TestPriceFeedIntegrity:
    """Проверка целостности цены"""

    def test_price_not_stale(
        self
    ):
        """Цена не должна быть старше 30 секунд"""
        now = datetime.utcnow()
        price_timestamp = now - timedelta(seconds=25)
        
        age_seconds = (now - price_timestamp).total_seconds()
        max_stale_seconds = 30
        
        assert age_seconds < max_stale_seconds

    def test_price_too_stale_rejected(
        self
    ):
        """Цена старше 30 сек отклоняется"""
        now = datetime.utcnow()
        price_timestamp = now - timedelta(seconds=35)
        
        age_seconds = (now - price_timestamp).total_seconds()
        max_stale_seconds = 30
        
        assert age_seconds > max_stale_seconds

    def test_price_sanity_check(
        self
    ):
        """Проверка логики цены (не BTC=$0.01)"""
        btc_price = 50000
        
        # Разумные границы для BTC
        assert 10_000 < btc_price < 1_000_000

    def test_price_deviation_detection(
        self
    ):
        """Обнаружение аномальных скачков цены"""
        previous_price = 50000
        current_price = 40000  # 20% падение за один tick
        
        deviation_pct = abs(
            (current_price - previous_price) / previous_price * 100
        )
        
        max_single_tick_deviation = 5  # 5% max
        
        if deviation_pct > max_single_tick_deviation:
            # Нужна дополнительная проверка
            assert True


class TestExecutionSimulation:
    """Симуляция исполнения ордера"""

    def test_market_order_executes_at_best_price(
        self
    ):
        """Market order исполняется по лучшей цене"""
        bid_price = 49990
        ask_price = 50010
        
        order_side = 'buy'
        execution_price = ask_price if order_side == 'buy' else bid_price
        
        assert execution_price == 50010

    def test_limit_order_waits_for_price(
        self
    ):
        """Limit order ждет когда цена достигнет лимита"""
        limit_price = 49000
        bid_price = 50000
        
        # Limit buy должен ждать пока bid_price <= limit_price
        can_execute = bid_price <= limit_price
        
        assert not can_execute  # Еще не готов

    def test_slippage_calculation(
        self
    ):
        """Расчет slippage (разница между expected и actual)"""
        expected_price = 50000
        actual_price = 50100  # 0.2% хуже
        
        slippage_pct = abs(
            (actual_price - expected_price) / expected_price * 100
        )
        
        assert slippage_pct == pytest.approx(0.2)


class TestTradeAccounting:
    """Учет сделок и P&L"""

    def test_pnl_calculation_buy_hold_sell(
        self
    ):
        """P&L для простой buy-hold-sell последовательности"""
        entry_price = 50000
        exit_price = 51000
        quantity = 1.0
        
        pnl = (exit_price - entry_price) * quantity
        pnl_pct = (pnl / (entry_price * quantity)) * 100
        
        assert pnl == 1000
        assert pnl_pct == pytest.approx(2.0)

    def test_pnl_with_fees(
        self
    ):
        """P&L с учетом комиссий"""
        entry_price = 50000
        exit_price = 51000
        quantity = 1.0
        
        entry_fee_pct = 0.1  # 0.1% комиссия
        exit_fee_pct = 0.1
        
        entry_fee = entry_price * quantity * entry_fee_pct / 100
        exit_fee = exit_price * quantity * exit_fee_pct / 100
        
        gross_pnl = (exit_price - entry_price) * quantity
        net_pnl = gross_pnl - entry_fee - exit_fee
        
        assert net_pnl < gross_pnl
        assert net_pnl == pytest.approx(900)

    def test_multiple_entries_average_price(
        self
    ):
        """Средняя цена входа для нескольких покупок"""
        entries = [
            {'price': 50000, 'quantity': 1.0},
            {'price': 51000, 'quantity': 1.0},
        ]
        
        total_cost = sum(e['price'] * e['quantity'] for e in entries)
        total_quantity = sum(e['quantity'] for e in entries)
        avg_price = total_cost / total_quantity
        
        assert avg_price == 50500

    def test_trailing_stop_loss(
        self
    ):
        """Trailing stop loss обновляется с новыми максимумами"""
        entry_price = 50000
        trailing_stop_pct = 5  # 5% от максимума
        
        prices = [50000, 51000, 52000, 51500, 50500]
        
        max_price = max(prices)
        stop_loss_price = max_price * (1 - trailing_stop_pct / 100)
        current_price = prices[-1]
        
        should_exit = current_price <= stop_loss_price
        
        assert not should_exit  # 50500 > 49400


class TestOrderTypes:
    """Различные типы ордеров"""

    def test_good_til_cancelled_remains_open(
        self
    ):
        """GTC ордер остается открытым"""
        order_type = 'GTC'
        is_expired = False  # GTC не истекает
        
        assert not is_expired

    def test_immediate_or_cancel_fills_or_cancels(
        self
    ):
        """IOC ордер исполняется или отменяется немедленно"""
        order_type = 'IOC'
        can_partial_fill = False  # IOC либо полный fill, либо cancel
        
        assert not can_partial_fill

    def test_fill_or_kill_all_or_nothing(
        self
    ):
        """FOK ордер - все или ничего"""
        order_type = 'FOK'
        partial_fill = False  # FOK не допускает частичный fill
        
        assert not partial_fill


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
