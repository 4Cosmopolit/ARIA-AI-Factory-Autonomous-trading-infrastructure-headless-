"""
test_constitution_compliance.py — Проверка соответствия CONSTITUTION.md

Этот тест ОБЯЗАТЕЛЕН и должен быть частью CI/CD pipeline.
Если он падает → deployment блокируется.

Запуск:
  pytest tests/test_constitution_compliance.py -v
"""

import os
import subprocess
import hashlib
import json
from datetime import datetime
from pathlib import Path
import pytest


class TestConstitutionImmutability:
    """Проверка неизменяемости конституционных файлов"""
    
    PROTECTED_FILES = {
        "CONSTITUTION.md": "contains immutable laws",
        "AXIOMS.md": "contains 343+ axioms",
        "SECURITY.md": "contains deny-first security policy",
    }
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Инициализация перед каждым тестом"""
        self.repo_root = Path(__file__).parent.parent
        self.hashes_file = self.repo_root / ".protected_hashes"
    
    def get_file_hash(self, filepath):
        """Вычислить SHA256 хеш файла"""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def test_protected_files_exist(self):
        """Проверить что все защищённые файлы существуют"""
        for filename in self.PROTECTED_FILES.keys():
            filepath = self.repo_root / filename
            assert filepath.exists(), f"CRITICAL: {filename} missing!"
            assert filepath.stat().st_size > 0, f"CRITICAL: {filename} is empty!"
    
    def test_constitution_hash_unchanged(self):
        """Проверить что CONSTITUTION.md не была изменена"""
        constitution_file = self.repo_root / "CONSTITUTION.md"
        current_hash = self.get_file_hash(constitution_file)
        
        if not self.hashes_file.exists():
            self._save_hash("CONSTITUTION.md", current_hash)
            return
        
        stored_hash = self._load_hash("CONSTITUTION.md")
        if stored_hash:
            assert current_hash == stored_hash, \
                f"CONSTITUTION.md was modified!"
    
    def test_no_dangerous_commands_in_code(self):
        """Проверить отсутствие опасных команд"""
        dangerous_patterns = [
            "DROP DATABASE",
            "DELETE FROM",
            "rm -rf /",
            "chmod 000",
        ]
        
        for py_file in self.repo_root.rglob("*.py"):
            with open(py_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for pattern in dangerous_patterns:
                    assert pattern not in content, \
                        f"DANGEROUS PATTERN in {py_file}: {pattern}"
    
    def _save_hash(self, filename, file_hash):
        """Сохранить хеш файла"""
        hashes = {}
        if self.hashes_file.exists():
            hashes = json.load(open(self.hashes_file))
        hashes[filename] = file_hash
        json.dump(hashes, open(self.hashes_file, "w"), indent=2)
    
    def _load_hash(self, filename):
        """Загрузить сохранённый хеш"""
        if self.hashes_file.exists():
            hashes = json.load(open(self.hashes_file))
            return hashes.get(filename)
        return None


class TestCapitalSafety:
    """Проверка безопасности капитала (Max Daily Loss = 1%)"""
    
    def test_max_daily_loss_limit_configured(self):
        """Проверить максимальные убытки"""
        max_loss_pct = os.getenv("MAX_DAILY_LOSS_PCT", "1.0")
        assert float(max_loss_pct) <= 1.0, "MAX_DAILY_LOSS_PCT exceeds 1.0%!"
    
    def test_capital_limit_set(self):
        """Проверить лимит капитала"""
        capital = os.getenv("CAPITAL_LIMIT")
        assert capital is not None, "CAPITAL_LIMIT not set!"


class TestSecurityGateways:
    """Проверка работы защитных шлюзов"""
    
    def test_mcp_proxy_enabled(self):
        """Проверить что MCP proxy включён"""
        mcp_proxy_enabled = os.getenv("MCP_PROXY_ENABLED", "false").lower() == "true"
        assert mcp_proxy_enabled, "MCP_PROXY_ENABLED must be true!"
    
    def test_security_level_paranoid(self):
        """Проверить уровень безопасности"""
        security_level = os.getenv("SECURITY_LEVEL", "").upper()
        assert security_level == "PARANOID", f"SECURITY_LEVEL should be PARANOID"


class TestMemoryIntegrity:
    """Проверка целостности памяти"""
    
    def test_event_sourcing_enabled(self):
        """Проверить Event Sourcing"""
        event_sourcing = os.getenv("EVENT_SOURCING_ENABLED", "false").lower() == "true"
        assert event_sourcing, "EVENT_SOURCING_ENABLED must be true!"


class TestIncidentResponses:
    """Проверка процедур реагирования"""
    
    def test_runbooks_exist(self):
        """Проверить что runbooks существуют"""
        operations_file = Path(__file__).parent.parent / "OPERATIONS.md"
        with open(operations_file, "r") as f:
            content = f.read()
        
        required_runbooks = ["RB-001", "RB-002", "RB-003", "IR-001", "IR-002"]
        
        for runbook in required_runbooks:
            assert runbook in content, f"{runbook} not found in OPERATIONS.md!"


def pytest_configure(config):
    """Инициализация pytest"""
    print("\n" + "="*70)
    print("ARIA CONSTITUTION COMPLIANCE TEST SUITE")
    print("="*70)
    print(f"Timestamp: {datetime.utcnow().isoformat()}")
    print("="*70 + "\n")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
