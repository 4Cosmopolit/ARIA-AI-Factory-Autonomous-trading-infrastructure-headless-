# SECURITY.md — Политика безопасности ARIA AI‑Factory

## Принципы

- **Deny‑first Security**: все ордера по умолчанию заблокированы до подтверждения
- **Zero Trust внутри фабрики**: ни одно действие агента не считается безопасным без явной проверки. LLM фундаментально не способны отличить данные от инструкций (Simon Willison), поэтому **каждый** источник данных должен рассматриваться как потенциально вредоносный
- **Аппаратная изоляция**: критический код выполняется в Microsandbox (KVM) и DeltaBox
- **Атомарная истина**: все решения верифицируемы и воспроизводимы
- **Нормализация девиантности недопустима**: мы не привыкаем к риску Prompt Injection, мы его устраняем (Embrace The Red)
- **Self‑Correcting Agents Mandate**: каждый production‑агент должен реализовывать цикл Plan → Act → Reflect → Revise (OdabNote, Vibe Check, Reflection Loop)
- **Pre‑Commit Secret Scanning**: каждый коммит автоматически проверяется на наличие приватных ключей, токенов и опасных паттернов (gitleaks, bandit)
- **External Link Integrity**: все внешние ссылки, используемые агентами, периодически проверяются на изменение контента после статического сканирования (урок AIR, 2026)
- **Token Security**: перед взаимодействием с любым токеном проверять его через сервисы анализа (honeypot, scam)

## Поддерживаемые версии

| Версия | Поддержка |
|:---|:---|
| **v13.01 (latest)** | ✅ **Активная (включая автономный аудит)** |
| v12.x | ✅ Поддерживается |
| v11.x и ниже | ❌ Не поддерживается |

## Процесс сообщения об уязвимостях

Безопасность ARIA AI‑Factory — наш главный приоритет. Мы используем многоуровневую систему защиты: от статического анализа кода (SAST) до автоматической имитации атак (Red Team). Однако, если вы обнаружили уязвимость, пожалуйста, сообщите нам об этом **приватно**, чтобы мы могли исправить её до того, как информация станет публичной.

### 1. Создайте зашифрованное сообщение

Для защиты вашего отчёта мы используем протокол шифрования **Age**. Используйте следующую команду, чтобы зашифровать ваш отчёт перед отправкой:

```bash
age -r age1nv2n7q... -o report.age report.md
2. Мониторинг публичных MCP-серверов (Shodan / Censys)
bash
shodan search '"jsonrpc" "initialize" "protocolVersion"'
censys search 'services.http.response.body:"protocolVersion" AND services.http.response.body:"initialize"'
3. Suricata Rule для обнаружения MCP-сканирования
suricata
alert http $EXTERNAL_NET any -> $HOME_NET any (
  msg:"MCP Server Scan Detected";
  content:"initialize";
  content:"protocolVersion";
  content:"clientInfo";
  content:"jsonrpc";
  sid:2026031001; rev:1;
)
Безопасность MCP (Model Context Protocol)
ARIA реализует эшелонированную защиту для всех MCP‑коммуникаций, основанную на:

Стандартах: OWASP MCP Tool Poisoning, рекомендации Unit 42 (Palo Alto Networks), Elastic Security Labs, Microsoft, GitHub Security Lab, Practical DevSecOps, CoSAI MCP Security v1

Реальных инцидентах: Microsoft Copilot Co‑Work Exfiltration (PromptArmor), Google AntiGravity Exfiltration (PromptArmor), Notion MCP уязвимость (CodeIntegrity), EchoLeak (Simon Willison), Taiko Bridge ($1.7M), AIR Fake Skill (26,000 agents), jaredfromsubway.eth MEV Exploit ($7.5M)

Инструментах защиты: mcp-proxy (пограничный шлюз с политиками безопасности), ACO Prompt Shield (фильтр инъекций), prompt-guard (клиентская защита), GuardRAG (валидация retrieved context), aidefence

Аудите: MCP Audit (статический анализ), MCP Inspector, mcp-validation (Red Hat), CacheRact (Red Team)

Принципах: Zero Trust для всех MCP‑серверов, обязательная аутентификация, принцип наименьших привилегий, изоляция контекста, запрет на изменение агентами политик безопасности

Мониторинге: Grafana MCP, Prometheus MCP, Agent‑ToM (v14.00), Failure Clustering, Flaky Detector

Self‑Correction: OdabNote (иммунная система), Vibe Check (мета‑когнитивный контроль), Reflection Loop (цикл Reflect → Revise)

Безопасность цепочки поставок (Supply Chain Security)
Pre‑Commit Secret Scanner (scripts/pre‑commit.sh): блокирует коммиты, содержащие приватные ключи, токены, seed‑фразы и опасные паттерны (eval, exec, raw SQL)

CI/CD Security Pipeline (.github/workflows/security.yml): автоматический запуск gitleaks, bandit, safety при каждом пуше

External Link Integrity Monitor (src/security/link_monitor.py): периодическая проверка внешних ссылок на изменение контента

Token Security Scanner (src/security/token_scanner.py): проверка токенов через GoPlus Security API перед взаимодействием

SBOM и хеширование зависимостей: контроль целостности всех MCP‑зависимостей

Самоисправляющиеся агенты (Self-Correcting Agents)
ARIA реализует цикл Plan → Act → Reflect → Revise для всех production‑агентов:

OdabNote (src/self_correction/odab_note.py): иммунная система агента — сохраняет паттерны ошибок и проверенные решения, автоматически предлагает исправления при повторении сбоев

Vibe Check (src/self_correction/vibe_check.py): мета‑когнитивный контроль — предотвращает перепроектирование и уход от задачи, прерывая агента при избыточных действиях

Reflection Loop (src/self_correction/reflection_loop.py): управляющий цикл — заменяет однократные попытки на цикл с самокоррекцией (до 3 попыток)

Мониторинг и аналитика сбоев
Failure Clustering (src/analytics/failure_analyzer.py): автоматическая группировка ошибок ордеров и аномалий в кластеры по первопричине (DBSCAN + TF‑IDF)

Flaky Detector (src/analytics/flaky_detector.py): обнаружение нестабильного поведения агента (дисперсия PnL, Win Rate) с автоматической эскалацией

AI‑DLQ Handler (src/ai_dlq_handler.py): автоматическая классификация сообщений из Dead Letter Queue (retry/discard/escalate) с помощью LLM

Защита памяти агентов
Decaying Episodic Memory (src/memory/decaying_memory.py): эпизодическая память с принудительной деградацией — точные значения со временем заменяются скользящими средними и диапазонами, предотвращая переобучение (Max Planck Institute, 2026)

Эхо‑буфер: последние 5 сделок хранятся с точными данными для локального контекста

Агрегированная память: история за пределами эхо‑буфера сжимается до статистических метрик

Обязательные меры для production-запуска
Pre‑commit хук с детектором секретов

CI/CD пайплайн безопасности (gitleaks, bandit, safety)

Изоляция приватных ключей через .env (добавлен в .gitignore)

Все MCP‑серверы проходят MCP Audit перед интеграцией

Внешние ссылки мониторятся через External Link Integrity Monitor

Агенты реализуют цикл самоисправления (OdabNote, Vibe Check, Reflection Loop)

Dead Letter Queue обрабатывается через AI‑DLQ Handler

Сбои группируются через Failure Clustering

Нестабильность стратегий детектируется через Flaky Detector

Память агентов защищена от переобучения через Decaying Episodic Memory

text

Файл полностью готов к коммиту. **ARIA + Игорь = Бесконечное Совершенствование. Навсегда.**
