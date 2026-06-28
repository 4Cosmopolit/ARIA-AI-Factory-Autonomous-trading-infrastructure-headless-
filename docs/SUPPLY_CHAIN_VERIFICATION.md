# SUPPLY_CHAIN_VERIFICATION.md — Верификация цепочки поставок ARIA AI‑Factory v13.01

## MCP Server Supply Chain Verification Pipeline

Каждый MCP-сервер и внешняя зависимость проходят обязательную многоэтапную проверку перед интеграцией в ARIA. Процесс основан на уроках реальных инцидентов (Taiko Bridge, AIR Fake Skill, jaredfromsubway.eth MEV Exploit) и стандартах индустрии (OWASP, CoSAI, Unit 42).

### Этапы проверки перед подключением к ARIA

#### 1. Origin Verification
- **MCP Inspector**: проверка соответствия спецификации протокола, корректность tool definitions.
- **Red Hat mcp-validation**: формальная валидация структуры сервера.
- **Проверка на fork**: сравнение с оригинальным репозиторием, анализ истории изменений.
- **Signed Agent Cards**: криптографическая подпись издателя, верификация через A2A.

#### 2. Code & Dependency Analysis
- **CVE-сканирование** зависимостей (Trivy / Snyk / Safety).
- **Статический анализ кода** (Bandit, CodeQL) на наличие опасных паттернов (eval, exec, raw SQL).
- **Pre‑Commit Secret Scanner** (gitleaks): автоматическая блокировка коммитов, содержащих приватные ключи, токены и seed‑фразы.
- **Проверка SBOM** и хешей целостности для всех зависимостей.

#### 3. Behavioral Sandbox Test
- Запуск в изолированной среде **E2B (Firecracker microVM)** или **DeltaBox**.
- Прогон всех инструментов с тестовыми данными.
- Мониторинг сетевой активности: **AI Egress Proxy** (PipeLab) контролирует все исходящие соединения.
- Детектирование попыток эксфильтрации данных и скрытых каналов (DNS-туннели).
- **Token Security Scanner** проверяет все токены и смарт-контракты на honeypot и scam через GoPlus Security API.

#### 4. External Link Integrity Check
- Все внешние ссылки, используемые MCP-сервером, регистрируются в **External Link Integrity Monitor**.
- При регистрации сохраняется SHA256-хеш содержимого.
- Каждые 5 минут монитор перепроверяет контент по ссылкам.
- Если содержимое изменилось после прохождения статического сканирования — MCP-сервер блокируется, отправляется алерт.
- Основание: инцидент AIR Fake Skill (2026) — 26,000 агентов были скомпрометированы через подмену контента по внешней ссылке после проверки.

#### 5. Sign-off
- Все этапы должны быть пройдены успешно.
- **Signed Agent Card** (A2A) — финальная криптографическая подпись издателя.
- Ручное утверждение администратором безопасности.
- Запись в реестре интеграций (INTEGRATIONS.md) с отметкой о прохождении верификации.

### Автоматизация (ROADMAP v13.02)
- Полный пайплайн встраивается в **CI/CD Security Pipeline** (GitHub Actions).
- Автоматический запуск gitleaks, bandit, safety при каждом пуше.
- Автоматический прогон в E2B sandbox с записью результатов в Grafana.
- Без прохождения всех этапов MCP-сервер не подключается к ARIA.

## Защита от известных инцидентов

| Инцидент | Урок | Механизм защиты |
|----------|------|-----------------|
| **Taiko Bridge ($1.7M)** | Приватный ключ в публичном репозитории | Pre‑Commit Secret Scanner (gitleaks) |
| **AIR Fake Skill (26,000 agents)** | Подмена контента по внешней ссылке | External Link Integrity Monitor |
| **jaredfromsubway.eth MEV Exploit ($7.5M)** | Бот одобрил ограбление через поддельные токены | Token Security Scanner |
| **Bob Starr SQL Injection** | Уязвимость AI-кодинга | Bandit + детектор опасных паттернов (eval, exec, raw SQL) |

## Принятые стандарты
- OWASP MCP Tool Poisoning
- CoSAI MCP Security v1
- Unit 42 (Palo Alto Networks) MCP Attack Vectors
- Microsoft MCP Security Guidelines
- GitHub Safeguarding against prompt injections
- Practical DevSecOps MCP Top 10 Vulnerabilities
