"""
conftest.py — Shared pytest fixtures and configuration

Provides:
- Global fixtures
- Environment setup
- Mock objects
"""

import pytest
import os
from datetime import datetime


@pytest.fixture(scope="session")
def test_env():
    """Setup test environment variables"""
    os.environ['ENVIRONMENT'] = 'test'
    os.environ['MAX_DAILY_LOSS_PCT'] = '1.0'
    os.environ['CAPITAL_LIMIT'] = '1000000'
    os.environ['HITL_THRESHOLD_USD'] = '500000'
    os.environ['MCP_PROXY_ENABLED'] = 'true'
    os.environ['SECURITY_LEVEL'] = 'PARANOID'
    yield
    # Cleanup


@pytest.fixture
def mock_capital_manager():
    """Mock Capital Manager"""
    class MockCapitalManager:
        def __init__(self):
            self.managed_capital = 1_000_000
            self.daily_loss = 0
            self.max_daily_loss = 10_000
        
        def check_order(self, order_size):
            remaining = self.max_daily_loss - self.daily_loss
            return order_size <= remaining
        
        def record_loss(self, loss_amount):
            self.daily_loss += loss_amount
    
    return MockCapitalManager()


@pytest.fixture
def mock_price_feed():
    """Mock Price Feed"""
    class MockPriceFeed:
        def __init__(self):
            self.prices = {
                'BTC/USD': 50000,
                'ETH/USD': 3000,
            }
            self.last_update = datetime.utcnow()
        
        def get_price(self, symbol):
            return self.prices.get(symbol)
        
        def update_price(self, symbol, price):
            self.prices[symbol] = price
            self.last_update = datetime.utcnow()
    
    return MockPriceFeed()


@pytest.fixture
def mock_memory():
    """Mock Memory System"""
    class MockMemory:
        def __init__(self):
            self.facts = {}
            self.events = []
        
        def store_fact(self, fact_id, fact_data):
            self.facts[fact_id] = fact_data
            self.events.append({
                'type': 'fact_stored',
                'fact_id': fact_id,
                'timestamp': datetime.utcnow(),
            })
        
        def get_fact(self, fact_id):
            return self.facts.get(fact_id)
        
        def query(self, query_text):
            return list(self.facts.values())
    
    return MockMemory()


@pytest.fixture
def mock_mcp_proxy():
    """Mock MCP-proxy Gateway"""
    class MockMCPProxy:
        def __init__(self):
            self.blocked_requests = 0
            self.allowed_requests = 0
        
        def validate_request(self, request):
            if 'malicious' in str(request).lower():
                self.blocked_requests += 1
                return False
            self.allowed_requests += 1
            return True
        
        def get_stats(self):
            return {
                'blocked': self.blocked_requests,
                'allowed': self.allowed_requests,
            }
    
    return MockMCPProxy()


def pytest_configure(config):
    """Configure pytest"""
    print("\n" + "="*70)
    print("ARIA SKILLS UNIT TESTS - Phase 2 v13.02")
    print("="*70)
    print(f"Start time: {datetime.utcnow().isoformat()}")
    print("="*70 + "\n")
