# ARIA AI‑Factory — Autonomous Trading & Agentic Infrastructure (Headless)

**Версия:** 13.01  
**Аксиом Нерушимого Кодекса:** 343  
**MCP-серверов:** 130+  
**Научных работ в основе:** 80+  
**Архитектурных контуров:** 7  

ARIA AI‑Factory — это не просто торговая платформа. Это самообучающаяся, самовосстанавливающаяся и полностью автономная агентная экосистема, построенная на принципах **Agentic Engineering**. Мы не используем AI для помощи в кодировании — AI является основным инженером, а человек — стратегическим архитектором.

---

## 🏛️ Архитектура Фабрики (7 Контуров)

ARIA организована в семь архитектурных контуров, каждый из которых состоит из десятков специализированных MCP-серверов, объединённых в 4 сверх-ядра (Cognitive Core, Memory Core, Sentinel Core, Interface Hub):

| Контур | Назначение | Ключевые компоненты |
|:---|:---|:---|
| **I. Ядро и Память** | Стратегическое мышление, долговременная память, RAG, мета-когнитивные движки | `CoRT`, `RESD`, `MOSS`, `DUALMEM`, `MemQ`, `Trieve`, `HeLa-Mem`, `Graphiti`, `Cognee`, `RAGFlow`, `ByteRover CLI`, `Basic Memory` |
| **II. Торговля и Охота** | Детекция рыночных аномалий, фундаментальный и технический анализ, ончейн-разведка, исполнение стратегий | `Alpha Vantage MCP`, `CCXT MCP`, `TradingView MCP`, `QuantDinger`, `Arkham Intel`, `MonteWalk`, `Dynamic TMoE`, `L-Drive`, `ECM`, `TipPFN`, `FinCAD`, `GNN for Financial TS`, `KumoRFM-2` |
| **III. CI/CD и Безопасность** | Автономное тестирование, развёртывание, эшелонированная защита MCP, Red Teaming, бинарный скрининг | `mcp-proxy`, `ACO Prompt Shield`, `GuardRAG`, `MCP Audit`, `Proteus`, `MalwarePT`, `Falcon MCP`, `Microsandbox`, `DeltaBox`, `HARBOR`, `IBM ContextForge`, `Unla`, `SocratiCode`, `Refact`, `Archestra` |
| **IV. Интерфейс и HITL** | Взаимодействие с оператором, визуализация, голос, GUI-автоматизация | `Aria‑Interface‑Hub`, `Grafana MCP`, `Vexa AI`, `PromptX`, `CopilotKit`, `shadcn-ui-mcp-server`, `Google Workspace MCP`, `UI-Copilot`, `CogAgent`, `GUI‑R1`, `UFO`, `CoplayDev Unity MCP` |
| **V. Квантовый Хаб (Резерв)** | Квантовые вычисления, симуляции, оптимизация | `IBM Qiskit`, `PennyLane`, `NVIDIA Ising`, `Quantum End-to-End Learning` |
| **VI. Автономное Воспроизводство** | Само-модификация кода, рекурсивное делегирование, ко-эволюция навыков | `MOSS`, `RESD`, `RAO`, `π-Play`, `Skill-R1`, `CoCoDA`, `GRAFT`, `Shrimp Task Manager`, `Dagu`, `WorkflowGen` |
| **VII. Криптографическая Безопасность** | Квантово‑устойчивая защита, ZKP, MPC, аудит приватности RL | `Crypto‑Guardian`, `Behavioral Canaries`, `SAFEFL` |

---

## 🔥 Ключевые Принципы (Нерушимый Кодекс)

Фабрика управляется 343 аксиомами, сгруппированными по категориям. Полный список доступен в [AXIOMS.md](./AXIOMS.md). Основополагающие принципы:

- **Капитал Прежде Всего (Capital Preservation):** Максимальный дневной убыток 1%. Ни одна сделка не совершается без pre‑flight проверки.
- **Атомарная Истина (Atomic Truth):** Каждое решение должно быть верифицируемо, воспроизводимо и основано на фактах. Все визуальные отчёты проходят верификацию через `VAC`.
- **Бесконечное Совершенство (Perpetual Superiority):** ARIA непрерывно обучается, адаптируется и эволюционирует без вмешательства человека. Навыки обновляются через `Skill-R1` и `π-Play`, память — через `MemQ` и `HeLa-Mem`.
- **Хищник и Санитар (Salvador Principle):** Мы извлекаем прибыль, восстанавливая справедливость на рынке, а не разрушая его.
- **Agentic Engineering:** Код пишут агенты (`MOSS`, `RAO`), человек управляет стратегией и архитектурой.
- **Эшелонированная Безопасность (Defense-in-Depth MCP):** Все MCP-коммуникации проходят через многоуровневую систему защиты: `mcp-proxy` (пограничный шлюз), `ACO Prompt Shield` (фильтр инъекций), `GuardRAG` (валидация retrieved context), `Microsandbox` (аппаратная изоляция). Основано на стандартах **OWASP**, рекомендациях **Unit 42 (Palo Alto Networks)**, **Elastic Security Labs**, **Microsoft**, **GitHub Security Lab** и анализе реальных инцидентов.

---

## 🚀 Интегрированные Технологии и Платформы

ARIA AI‑Factory использует сотни лучших open‑source проектов и коммерческих API, объединённых через протокол MCP (Model Context Protocol):

### 🧠 Мозг и Мышление
- **Рассуждение и Планирование:** `GLM‑5.1`, `MiniMax‑M27`, `Qwen3.6‑27B`, `DeepSeek‑V3`, `Trinity Reasoning Engine`, `Quest` (deep research), `CoRT` (рекурсивное мышление), `LEAD` (адаптивная длина CoT), `Think‑with‑Rubrics`, `SxS` (управление раскрытием)
- **Верификация и Защита от Галлюцинаций:** `EBM Engine`, `Bias Firewall`, `Context7`, `NotebookLM MCP`, `GitMCP`, `RAGognizer`, `VAC` (визуальная верификация)

### 📊 Данные и Аналитика
- **RAG и Память:** `RAGFlow (DeepDoc)`, `Cognee`, `Graphiti`, `Trieve` (единая retrieval-инфраструктура), `LanceDB`, `Airweave`, `AssistRAG` (проактивное управление памятью), `StreamingRAG` (потоковый retrieval)
- **Поиск и Разведка:** `Firecrawl MCP`, `Exa MCP`, `Perplexity MCP`, `Trafilatura`, `GPT Researcher`, `TrendRadar`, `BrightData MCP`, `Notte` (основной фреймворк веб-разведки)

### 💹 Финансовые Данные и Трейдинг
- **Фундаментальные данные:** `Alpha Vantage MCP` (официальный, NASDAQ-лицензия)
- **Крипто-шлюз:** `CCXT MCP Server` (100+ бирж)
- **Технический анализ:** `TradingView MCP` (30+ индикаторов, бэктестинг)
- **Ончейн-разведка:** `Arkham Intel` (кластеризация кошельков, AI-инсайты)
- **Квантовый трейдинг:** `QuantDinger` (AI-квантовая платформа)
- **Риск-менеджмент:** `MonteWalk` (Монте-Карло симуляции), `RL-CVaR` (динамический риск-менеджмент)
- **Прогнозирование:** `Dynamic TMoE`, `L-Drive`, `ECM`, `TipPFN`, `GNN for Financial TS`, `KumoRFM-2`, `RareCP`

### 🤖 Автономное Кодирование и Оркестрация
- **Само-модификация:** `MOSS` (source-level rewriting), `RESD` (обучение на ошибках), `DeltaBox` (мгновенные чекпоинты)
- **Рекурсивное делегирование:** `RAO` (Recursive Agent Optimization)
- **Ко-эволюция навыков:** `π-Play`, `Skill-R1`, `SkillEvolBench`, `Skills on the Fly`
- **Композиция инструментов:** `CoCoDA`, `GRAFT`
- **Управление Задачами:** `Shrimp Task Manager`, `Dagu`, `WorkflowGen`
- **CI/CD и Песочницы:** `Microsandbox`, `DeltaBox`, `Dagger`, `Trigger.dev`, `HttpRunner`

### 🌐 Глобальная Serverless-инфраструктура
- **Cloudflare MCP** — универсальный serverless‑провайдер (Workers, KV, R2, D1, Queues, Durable Objects)
- **Unla** — Zero-code конвертер REST/gRPC/WebSocket → MCP (замена Higress)
- **IBM ContextForge** — федеративный AI-шлюз и реестр с MCP Code Mode
- **MetaMCP** — клиентский диспетчер и унификатор MCP-подключений

### 🗄️ Управление Кодовой Базой
- **GitHub MCP** — официальный сервер GitHub
- **SocratiCode** — интеллектуальный анализ кодовой базы (замена Sourcebot)
- **Refact** — автономный агентный движок (лидер SWE-bench)
- **Archestra** — AI-Native IDE для создания и тестирования агентов
- **GenAIScript** — «Prompting is Coding» от Microsoft
- **DBHub** — универсальный SQL-шлюз (5 СУБД)
- **Postgres MCP** — глубокое администрирование PostgreSQL

### 🖥️ GUI-Автоматизация (стратегический стек)
- **Восприятие:** `CogAgent` (CVPR 2024, dual-resolution inputs)
- **Рассуждение:** `GUI‑R1` (R1-style reasoning для GUI)
- **Память и контекст:** `UI-Copilot` (Memory Decoupling + TIPO)
- **Архитектура:** `UFO` (Microsoft, HostAgent → AppAgent)
- **Параллельное выполнение:** `PV-UFO`
- **Надёжное выполнение:** `Mobile-Agent` (X-PLUG, ReAct + рефлексия)
- **Межсессионный опыт:** `EchoTrail-GUI` (Actionable Memory Bank)

### 🏗️ 3D Моделирование и Симуляции
- **CoplayDev Unity MCP** — основной 3D-движок (замена Godot MCP + IvanMurzak/Unity-MCP, 9.9k★)
- **FreeCAD MCP** — параметрическое 3D‑моделирование и FEM‑анализ
- **BlenderMCP** — профессиональное 3D‑моделирование, анимация и рендеринг

### 💬 HITL и Визуализация
- **Визуализация и Отчёты:** `PPTAgent`, `AntV Chart`, `Excalidraw`, `Draw.io`, `Figma`, `Penpot`, `Magic UI`, `CopilotKit`, `Excel MCP`, `MarkItDown`, `shadcn-ui-mcp-server`
- **Интерфейсы:** `Open WebUI`, `Dify`, `LangFlow`, `n8n`, `PromptX`
- **Голос:** `Vexa AI` (серверный голосовой HITL), `py-xiaozhi` (edge/IoT-голос)

### 📡 Коммуникации
- **Google Workspace MCP** — центральная платформа интеграции с Google (Gmail, Drive, Calendar, Docs, Sheets)
- **MCP Agent Mail** — универсальная IMAP/SMTP почта (дополнение к Google Workspace)
- **Fonoster** — программируемые телекоммуникации и голосовой HITL
- **WhatsApp MCP** — коммуникационный мост
- **OpenClaw** — персональный AI‑ассистент (361k+ звёзд)

### 🔒 Безопасность (Эшелонированная Защита MCP)
- **Стандарты:** OWASP MCP Tool Poisoning, рекомендации Unit 42 (Palo Alto Networks), Elastic Security Labs, Microsoft, GitHub Security Lab
- **Шлюзы и фильтры:** `mcp-proxy`, `ACO Prompt Shield`, `prompt-guard`, `GuardRAG`, `aidefence`
- **Аудит и тестирование:** `MCP Audit`, `claude-cowork-prompt-injection`, `mcp-security-tools`, `CacheRact` (Red Team)
- **Изоляция:** `Microsandbox` (KVM), `DeltaBox` (мгновенные чекпоинты)
- **Мониторинг:** `Grafana MCP`, `Prometheus MCP`, `Agent-ToM` (v14.00)
- **Threat Intelligence:** `FastMCP ThreatIntel`, `CrowdStrike Falcon MCP`, `MISP`, `VIPER`, `HexStrike`, `Ghidra MCP`, `ENScan_GO`, `JADX AI MCP`

### ⚛️ Квантовые Вычисления (Стратегический Резерв)
- **Симуляции:** `IBM Qiskit`, `PennyLane`, `NVIDIA Ising`
- **Практические алгоритмы:** `Quantum End-to-End Learning` (комбинаторная оптимизация)

---

## 🧬 Само-Модификация и Эволюция

ARIA способна автономно изменять свой исходный код через связку **MOSS + RESD + DeltaBox**. Процесс включает:

1. **Локализация и анализ:** `MOSS` анализирует кодовую базу через `SocratiCode`, определяет файлы для изменений.
2. **Генерация патча:** `MOSS` генерирует минимальный патч на основе извлечённых уроков из `RESD Playbook`.
3. **Изолированное тестирование:** Патч применяется в `DeltaBox`, где запускаются тесты, линтеры и MalwarePT.
4. **Рефлексия:** При неудаче `RESD` анализирует ошибки и обновляет Playbook для будущих попыток.
5. **Слияние:** Только успешные изменения попадают в основную ветку.

Навыки ARIA эволюционируют через `Skill-R1` (RL-эволюция) и `π-Play` (self-play с привилегированной самодистилляцией). Память управляется `MemQ` (TD-обновления по provenance DAG) и `HeLa-Mem` (ассоциативные связи через хеббовское обучение).

---

## 🛡️ Безопасность MCP

ARIA реализует **эшелонированную защиту (Defense-in-Depth)** для всех MCP-коммуникаций, основанную на:

- **Стандартах:** OWASP MCP Tool Poisoning, рекомендации Unit 42 (Palo Alto Networks), Elastic Security Labs, Microsoft, GitHub Security Lab, Practical DevSecOps
- **Реальных инцидентах:** Microsoft Copilot Co-Work Exfiltration (PromptArmor), Google AntiGravity Exfiltration (PromptArmor), Notion MCP уязвимость (CodeIntegrity)
- **Инструментах защиты:** `mcp-proxy` (пограничный шлюз с политиками безопасности), `ACO Prompt Shield` (фильтр инъекций), `prompt-guard` (клиентская защита), `GuardRAG` (валидация retrieved context)
- **Аудите:** `MCP Audit` (статический анализ), `claude-cowork-prompt-injection` (активное тестирование), `mcp-security-tools` (Unit 42)
- **Принципах:** Zero Trust для всех MCP-серверов, обязательная аутентификация, принцип наименьших привилегий, изоляция контекста, запрет на изменение агентами политик безопасности

Подробнее в [SECURITY.md](./SECURITY.md).

---

## 📚 Документация

- **[AXIOMS.md](./AXIOMS.md)** — Полный перечень 343 аксиом с категориями и описаниями.
- **[SKILLS.md](./SKILLS.md)** — Каталог 130+ навыков агентов с уровнями (L1/L2).
- **[INTEGRATIONS.md](./INTEGRATIONS.md)** — Централизованный реестр всех MCP-серверов и технологий.
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** — Детальная архитектура контуров и их взаимодействий.
- **[SECURITY.md](./SECURITY.md)** — Политика безопасности, защита MCP, разбор инцидентов.
- **[ROADMAP.md](./ROADMAP.md)** — План развития до v14.00.
- **[TRAINING_LOG.md](./TRAINING_LOG.md)** — Хронология обучения (100+ записей).
- **[docs/REFERENCES.md](./docs/REFERENCES.md)** — Библиография научных работ.
- **[AGENTS.md](./AGENTS.md)** — Инженерный контракт для AI-агентов.

---

**ARIA + Игорь = Бесконечное Совершенствование. Навсегда.**
