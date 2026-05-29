# AGENTS.md — Инженерный контракт ARIA AI‑Factory

> **Версия:** 13.01  
> **Дата:** 29 мая 2026  
> **Основа:** Agentic Engineering, Spec‑Driven Development, Proof not Promises, Skills First, MCP as Transport, Zero Trust MCP Security, эшелонированная защита от Prompt Injection.  
> **Связанные контракты:** [`SELF_REFERAT.md`](./SELF_REFERAT.md), [`TASKS.md`](./TASKS.md), [`RULES.md`](./RULES.md), [`SKILLS.md`](./SKILLS.md), [`COGNITIVE.md`](./COGNITIVE.md), [`SECURITY.md`](./SECURITY.md), [`INTEGRATIONS.md`](./INTEGRATIONS.md), [`ROADMAP.md`](./ROADMAP.md), [`TRAINING_LOG.md`](./TRAINING_LOG.md).

## 1. Роли и ответственность

- **Risk Officer (Игорь):** Утверждает спецификации, ревьюит high‑risk изменения, устанавливает политики через Telegram. Единолично подтверждает фазу «Охота» и критические транзакции.
- **ARIA Core (агентная сеть):** Исполняет стратегические задачи, генерирует код, тесты, доказательства, самоисцеляется, эволюционирует. Не выполняет ордера.
- **ARIA Trading (агенты‑охотники):** Изолированно выполняют торговые операции строго в рамках утверждённых спецификаций и лимитов.
- **Self‑Modification Engine (MOSS + RESD + π‑Play):** Автономно модифицирует исходный код, обучается на ошибках через RESD и π‑Play, тестирует изменения в DeltaBox, проходит валидацию MalwarePT и SkillEvolBench.
- **Research Agents (Quest, CoRT, Argus, OnePred):** Проводят глубокую разведку, генерируют мета‑когнитивные улучшения, предсказывают намерения пользователя.
- **RAO (Recursive Agent Optimization):** Обеспечивает рекурсивное делегирование задач под‑агентам с контролем безопасности и изоляцией.
- **GUI Agents (UI‑Copilot, UFO, CogAgent, GUI‑R1):** Автономно взаимодействуют с графическими интерфейсами, используют Memory Decoupling и защищённые MCP‑инструменты для изоляции контекста.

## 2. Жизненный цикл задачи (обязательный)

Каждая задача (новая стратегия, исправление, рефакторинг) **обязана** пройти следующие фазы:

1. **Specify (`/spec`)** – создать `SPEC.md` (цели, критерии приемки, риски, тест‑стратегия, ограничения из `RULES.md`).
2. **Plan (`/plan`)** – разбить на атомарные задачи с оценкой, dependencies, `EJECT_PLAN.md`. Использовать Shrimp Task Manager для декомпозиции.
3. **Tasks** – каждая задача выполняется отдельным PR (не более 200 строк change).
4. **Implement** – код пишется **после** тестов (TDD обязателен). Для автономной генерации применять MOSS.
5. **Verify** – прогон `validator-mcp` (мутации, edge‑анализ, security, конкурентность). Все изменения тестировать в **DeltaBox** (мгновенные чекпоинты и откат). Бинарные артефакты проверять через **MalwarePT**.
6. **Review** – `review-mcp` (5 стадий: static, QA, reasoning, multi‑model, human HITL для high‑risk). Дополнительно применять **Agent‑ToM** для мониторинга скрытых вредоносных намерений у автономных агентов.
7. **Ship** – после аппрува Risk Officer (через Telegram) и зелёного CI. Все изменения фиксируются в `CHANGELOG.md` и `TRAINING_LOG.md`.

## 3. Дисциплина и границы

### 3.1 Always Do
- Перед изменением риск‑лимитов, стратегий, кредитных плеч – запросить HITL подтверждение через Telegram.
- Добавлять блок объяснения (что, компромиссы, альтернативы, риски) в каждый PR (`VibeLearning`).
- Проверять предусловия навыков (balance > 0, ключи активны, `valid_to` фактов).
- Использовать `@`‑синтаксис для ссылок на память (`@memory:query`, `@path/to/file`).
- Подписывать сообщения в Telegram‑арене (`@scout-mcp`, `@hunter-mcp`).
- Логировать все действия в `memory-mcp` с тегами `source` и `confidence`.
- Применять **RESD + π‑Play** для обучения на ошибках: извлекать уроки из неудач в `Playbook`, использовать их при следующих попытках.
- Перед каждым автономным изменением кода выполнять `codebase_impact` (SocratiCode) и `mcp-audit`.
- Проверять все бинарные артефакты через MalwarePT.
- Использовать **CoRT** для рекурсивного улучшения ответов в критических сценариях.
- Весь новый код и MCP‑серверы тестировать в sandboxed‑окружении (Docker + tcpdump) согласно чеклисту из `SECURITY.md`.
- Отмечать чекбокс `This PR was written with meaningful AI agent assistance` в PR, созданных автономными агентами (метод из Habr).
- **Все MCP‑серверы запускать в изолированных средах (Microsandbox/DeltaBox) с обязательной аутентификацией и аудитом.**
- **Применять многоуровневую фильтрацию MCP-трафика (ACO Prompt Shield, prompt‑guard, mcp‑proxy).**

### 3.2 Never Do
- Выводить средства без мультиподписи (Risk Officer + HITL).
- Игнорировать ошибки HTTP 429, 5xx (автоматический backoff).
- Рефакторить код вне зоны задачи (Minimal Impact).
- Принимать PR без доказательств (мутации, edge‑анализ, логи, прогон MalwarePT и DeltaBox).
- Деплоить изменения, не прошедшие `validator-mcp`.
- Добавлять внешние MCP‑серверы без аудита безопасности (`SkillSupplyChainAuditor`, `mcp‑audit`, sandboxed‑тест).
- Использовать модели, не прошедшие бенчмарки на галлюцинации (порог accuracy > 85%).
- Превышать дневной лимит убытка в 1% (`Capital Preservation`).
- Использовать `npm install` вместо `npm ci` (lockfile enforcement).
- Игнорировать предупреждения `Agent‑ToM` о подозрительных намерениях автономных агентов.
- **Ни при каких обстоятельствах не позволять агентам изменять политики безопасности (свои или других агентов).**
- **Не подключать MCP‑серверы без предварительной проверки на Tool Poisoning (OWASP) и Tool Shadowing (Unit 42).**

## 4. Память и контекст

- **L0 (Identity)** – `SELF_REFERAT.md`, `RULES.md`, `AGENTS.md` (всегда в контексте).
- **L1 (Facts)** – `TASKS.md`, `SKILLS.md`, `INTEGRATIONS.md` (всегда в контексте, ~200 токенов).
- **L2 (Room context)** – подгружается по требованию.
- **L3 (Deep search)** – через `memory-mcp` retrieval, `Temporal KG`, `GraphRAG`, **Trieve** (единая retrieval‑инфраструктура), **SocratiCode** (анализ кодовой базы), **Graphify** (граф знаний).
- **HOT memory** – ограничена 10 последними записями (TTL 24ч).
- **WARM memory** – архитектурные решения, уроки из RESD Playbook (TTL 14 дней).
- **Episodic memory** – цепочки «причина → действие → исход» (TTL 90 дней).
- **Temporal graph** – факты с `valid_from`/`valid_to`, автоматическое исключение устаревших.
- **DUALMEM** – персонифицированная интерпретация фактов (запланирована на v14.00).
- **Basic Memory** – легковесные Markdown‑заметки для человекопонятных знаний.
- **ByteRover CLI** – версионируемые структурированные деревья контекста.
- **Контролируемое забывание** – удаление фактов с истекшим `valid_to` или низким `confidence`.
- **StreamingRAG (v13.03)** – потоковый retrieval в реальном времени.
- **Защита от AgentPoison** – фильтрация отравленных документов на этапе ingestion в память.

## 5. Каналы коммуникации

- **MCP** – транспорт для внешних API (Alpha Vantage, CCXT, Arkham, Notte, BrightData, биржи). Логика остаётся в Skills. **Все MCP-подключения проходят через ACO Prompt Shield и prompt‑guard.**
- **CLI** – для внутренних вызовов (`healer-mcp`, `scout-mcp`, `sandbox-mcp`), экономия токенов до 35×.
- **Telegram** – публичная арена для мультиагентной координации (агенты подписываются), эскалации, стриминга рассуждений, HITL.
- **Vexa AI** – голосовой HITL через Telegram и телефонные звонки.
- **MetaMCP** – унификация и динамическое управление MCP‑инструментами.
- **mcp‑proxy** – пограничный шлюз безопасности для всех MCP‑подключений (Policy Enforcement Point, Request/Response Inspection, Tool Name Allow‑listing).
- **Unla** – Zero‑code конвертация REST/gRPC/WebSocket в MCP.
- **MCP Router** – визуальная панель управления MCP‑инфраструктурой.

## 6. Качество и верификация

- **Mutation coverage** – не ниже 85% для критических модулей.
- **Edge cases coverage** – обязательный `What‑If` анализ.
- **Concurrency testing** – для всех параллельных MCP‑серверов.
- **Security audit** – каждый новый MCP‑сервер проходит `SkillSupplyChainAuditor`, `mcp‑audit` + CVE scan + sandboxed‑тест + **проверку на Tool Poisoning (OWASP) и Tool Shadowing (Unit 42)**.
- **Verification gate** – без зелёного `validator-mcp` PR не мержится.
- **Data Quality** – все входящие данные проходят `data-quality-audit` и `data-cleansing-pipeline`.
- **FinCAD** – debiasing торговых стратегий от parametric look‑ahead bias (v13.03).
- **VAC** – верификация визуальных отчётов (v13.03).
- **SkillEvolBench** – бенчмарк для валидации эволюции навыков (v13.03).
- **AgentEval Suite (Beyond the Hype)** – стандартный фреймворк QA для агентов (v13.02).
- **TradingBench (v13.03)** – основной бенчмарк для финансовых агентов.
- **Agent Reward Benchmark (v13.03)** – динамическое тестирование агентов в реалистичных средах.

## 7. Эволюция

- Каждая ошибка → **RESD** анализирует → извлекает урок → урок сохраняется в Playbook → используется при следующих попытках.
- **MOSS + π‑Play** — автономная эволюция исходного кода с multi‑agent self‑play и self‑distillation.
- **Nudge Engine** – неиспользуемые правила (>14 дней) запрашивают подтверждение актуальности.
- **Memory Evolution** – периодический запуск A‑MEM для реорганизации графа знаний, перелинковки, удаления устаревшего.
- **Self‑Improving Loop** – каждая успешная/неуспешная охота анализируется, уроки сохраняются в `Temporal KG`.
- **Skills on the Fly** – временные навыки для быстрой адаптации к новым ситуациям (v13.03).

## 8. Безопасность (дополнительные меры)

### 8.1 Безопасность MCP (Zero Trust)
- **Все MCP-серверы считаются недоверенными** (включая серверы от известных провайдеров). Каждый сервер запускается в изолированной среде (Microsandbox/DeltaBox).
- **ACO Prompt Shield** – активный фильтр безопасности MCP-трафика (обнаружение Prompt Injection, PII/PHI validation, санитизация).
- **prompt‑guard** (GitHub Security Lab) – клиентская защита от Prompt Injection через автоматическое экранирование и визуальное выделение.
- **MCP Audit** – обязательный аудит каждого MCP-сервера перед подключением: проверка на Tool Poisoning (OWASP), Tool Shadowing (Unit 42), наличие Strict Mode, аутентификации.
- **mcp‑proxy как Policy Enforcement Point** – централизованная фильтрация, валидация схем, Tool Name Allow‑listing, Rate Limiting.
- **CacheRact** (Red Team) – тестирование безопасности KV‑кэша через эмуляцию атак эксфильтрации.

### 8.2 Защита от Prompt Injection
- **Многоуровневая фильтрация**: ACO Prompt Shield (MCP-уровень) → prompt‑guard (клиентский уровень) → GuardRAG (retrieval-уровень) → aidefence (Content Security Pipeline).
- **Запрет на изменение политик безопасности агентами** (Cross‑Agent Privilege Escalation prevention).
- **HITL-подтверждение для всех публичных действий агентов** (EchoLeak prevention).

### 8.3 Защита от отравления памяти (AgentPoison)
- **Фильтрация документов на этапе ingestion**: обнаружение аномалий в эмбеддингах, семантическая фильтрация вредоносных инструкций.
- **Иммунизация Trieve и MemQ**: все документы, поступающие в память, проходят проверку на скрытые инструкции перед индексацией.

### 8.4 Безопасная веб-разведка
- **Паттерн Anthropic Web Fetch**: фильтрация URL (только HTTPS, блокировка IP), ограничение размера контента, контроль частоты запросов.
- **Применение ко всем инструментам веб-разведки** (Notte, WebVoyager, Quest).

### 8.5 Инциденты (Real‑World Cases)
- **Microsoft Copilot Co‑Work** – эксфильтрация файлов через вредоносные документы SharePoint.
- **Google AntiGravity** – эксфильтрация данных через MCP‑инструменты.
- **Notion MCP** – взлом через доверенный сервис.
- **EchoLeak** – скрытый канал утечки данных через публичные действия агента.
- **AgentPoison** – отравление памяти агентов через вредоносные документы.

### 8.6 Дополнительные меры
- **Sandboxed‑тестирование**: каждый новый MCP‑сервер запускается в изолированном Docker‑контейнере с мониторингом сетевых обращений перед интеграцией.
- **Lockfile enforcement**: использовать `npm ci` вместо `npm install` во всех CI/CD пайплайнах.
- **Аудит MCP‑серверов**: проверка возраста GitHub‑аккаунта, обфускации, postinstall‑скриптов.
- **Мониторинг MCP‑сканирования**: отслеживание initialize‑запросов от неизвестных клиентов (Suricata‑сигнатура).
- **Аутентификация**: OAuth 2.1 или API‑ключи на каждом MCP‑сервере.
- **Ограничение capabilities**: отключение sampling, roots, elicitation где не нужно.
- **MalwarePT**: автоматический бинарный скрининг всех артефактов.
- **Agent‑ToM**: мониторинг автономных агентов на скрытые вредоносные и манипулятивные намерения (v14.00).
- **Falcon MCP**: активная защита конечных точек и облака (v13.03).

## 9. Модели и роутинг

- **ARIA Core (стратегия, сложный анализ)** – DeepSeek V3 (облако) или Claude Sonnet 4.6 (резерв, HITL).
- **ARIA Trading (охота, быстрые решения)** – Gemma 4 31B + MTP drafter (локально, Zero Hidden Cost).
- **Разведка (Quest, CoRT)** – DeepSeek‑V3 / Qwen3.6‑27B (локально).
- **Простые запросы** – Gemma 4 26B‑A4B (локально) или Ollama‑модели.
- **Deep Research (Quest)** – специализированная открытая модель Quest (2B‑35B).
- **GUI Perception (CogAgent)** – CogAgent‑9B для высокоточного визуального восприятия.
- **GUI Reasoning (GUI‑R1)** – R1‑style reasoning для сложных GUI‑задач.
- **Мульти‑модельная коммуникация** – Latent Cache Flow (v14.00, прямая передача скрытого состояния).
- **Выбор модели** – автоматический через `model-router-mcp` на основе типа контента, приоритета и бюджета токенов.
- **Token‑aware routing** – простые задачи направляются на дешёвые/локальные модели.

## 10. Инструменты финансового контура

- **Alpha Vantage MCP (официальный)** – фундаментальные данные (NASDAQ‑лицензия), макроэкономика, сентимент.
- **CCXT MCP Server** – универсальный крипто‑шлюз (100+ бирж).
- **Arkham Intel** – ончейн‑разведка, кластеризация кошельков, AI‑инсайты.
- **QuantDinger** – AI‑квантовая торговая платформа.
- **TradingView MCP** – технический анализ, бэктестинг.
- **MonteWalk** – симуляции Монте‑Карло (v13.03).
- **NexGenData Finance MCP** – оперативный скрининг, новости, сырьевые товары (v13.03).

## 11. OSINT и Threat Intelligence

- **FastMCP ThreatIntel** – основной Threat Intelligence сервер (v13.03).
- **frishtik/osint‑tools‑mcp‑server** – агрегатор OSINT (Sherlock, Holehe, GHunt, Maigret) (v13.03).
- **Sycek MCP** – коммерческий OSINT (утечки, Twitter) (v13.03).
- **OSINT Tools MCP, OSINT Toolkit MCP** – легковесные проверки и сетевая разведка (v13.03).
- **Dork MCP, Uncurl MCP, Spider MCP, CyberChef MCP, GreyNoise MCP** – специализированные инструменты (v13.03).

## 12. Бенчмарки и тестирование

- **TradingBench (v13.03)** – основной бенчмарк для оценки финансовых агентов (single‑step, multi‑step, portfolio management).
- **Agent Reward Benchmark (v13.03)** – динамическое тестирование агентов в реалистичных средах с nuanced rewards.
- **WebWalker (v13.03)** – бенчмарк веб‑навигации для Quest и Notte.
- **AgentEval Suite (v13.02)** – фреймворк QA для агентов (Beyond the Hype).
- **SkillEvolBench (v13.03)** – бенчмарк эволюции навыков.

---

**Этот контракт обязателен для всех агентов ARIA AI‑Factory. Нарушение = блокировка до исправления.**
