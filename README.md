# ARIA AI‑Factory — Autonomous Trading & Agentic Infrastructure (Headless)

**Версия:** 13.01 (updated 28.06.2026)  
**Аксиом Нерушимого Кодекса:** 420  
**MCP-серверов:** 130+  
**Научных работ в основе:** 80+  
**Архитектурных контуров:** 7  
**Архитектурных паттернов:** 12  

ARIA AI‑Factory — это не просто торговая платформа. Это самообучающаяся, самовосстанавливающаяся и полностью автономная агентная экосистема, построенная на принципах **Agentic Engineering**. Мы не используем AI для помощи в кодировании — AI является основным инженером, а человек — стратегическим архитектором.

---

## 🏛️ Архитектура Фабрики (7 Контуров)

ARIA организована в семь архитектурных контуров, каждый из которых состоит из десятков специализированных MCP-серверов, объединённых в 4 сверх-ядра (Cognitive Core, Memory Core, Sentinel Core, Interface Hub):

| Контур | Назначение | Ключевые компоненты |
|:---|:---|:---|
| **I. Ядро и Память** | Стратегическое мышление, долговременная память, RAG, мета-когнитивные движки, Compile-Time RAG | `CoRT`, `RESD`, `MOSS`, `DUALMEM`, `MemQ`, `Trieve`, `HeLa-Mem`, `Graphiti`, `Cognee`, `RAGFlow`, `ByteRover CLI`, `Basic Memory`, `Knowledge Compiler` |
| **II. Торговля и Охота** | Детекция рыночных аномалий, фундаментальный и технический анализ, ончейн-разведка, исполнение стратегий | `Alpha Vantage MCP`, `CCXT MCP`, `TradingView MCP`, `QuantDinger`, `Arkham Intel`, `MonteWalk`, `Dynamic TMoE`, `L-Drive`, `ECM`, `TipPFN`, `FinCAD`, `GNN for Financial TS`, `KumoRFM-2`, `Hunter 6.0` |
| **III. CI/CD и Безопасность** | Автономное тестирование, развёртывание, эшелонированная защита MCP, Red Teaming, бинарный скрининг, Self-Correction | `mcp-proxy`, `ACO Prompt Shield`, `GuardRAG`, `MCP Audit`, `Proteus`, `MalwarePT`, `Falcon MCP`, `Microsandbox`, `DeltaBox`, `HARBOR`, `IBM ContextForge`, `Unla`, `SocratiCode`, `Refact`, `Archestra`, `OdabNote`, `Vibe Check`, `Reflection Loop`, `Failure Clustering`, `Flaky Detector`, `AI-DLQ Handler` |
| **IV. Интерфейс и HITL** | Взаимодействие с оператором, визуализация, голос, GUI-автоматизация | `Aria‑Interface‑Hub`, `Grafana MCP`, `Vexa AI`, `PromptX`, `CopilotKit`, `shadcn-ui-mcp-server`, `Google Workspace MCP`, `UI-Copilot`, `CogAgent`, `GUI‑R1`, `UFO`, `CoplayDev Unity MCP` |
| **V. Квантовый Хаб (Резерв)** | Квантовые вычисления, симуляции, оптимизация | `IBM Qiskit`, `PennyLane`, `NVIDIA Ising`, `Quantum End-to-End Learning` |
| **VI. Автономное Воспроизводство** | Само-модификация кода, рекурсивное делегирование, ко-эволюция навыков | `MOSS`, `RESD`, `RAO`, `π-Play`, `Skill-R1`, `CoCoDA`, `GRAFT`, `Shrimp Task Manager`, `Dagu`, `WorkflowGen` |
| **VII. Криптографическая Безопасность** | Квантово‑устойчивая защита, ZKP, MPC, аудит приватности RL | `Crypto‑Guardian`, `Behavioral Canaries`, `SAFEFL` |

---

## 🔥 Ключевые Принципы (Нерушимый Кодекс)

Фабрика управляется 420 аксиомами, сгруппированными по категориям. Полный список доступен в [AXIOMS.md](./AXIOMS.md). Основополагающие принципы:

- **Капитал Прежде Всего (Capital Preservation):** Максимальный дневной убыток 1%. Ни одна сделка не совершается без pre‑flight проверки.
- **Атомарная Истина (Atomic Truth):** Каждое решение должно быть верифицируемо, воспроизводимо и основано на фактах.
- **Бесконечное Совершенство (Perpetual Superiority):** ARIA непрерывно обучается, адаптируется и эволюционирует без вмешательства человека.
- **Хищник и Санитар (Salvador Principle):** Мы извлекаем прибыль, восстанавливая справедливость на рынке, а не разрушая его.
- **Agentic Engineering:** Код пишут агенты (`MOSS`, `RAO`), человек управляет стратегией и архитектурой.
- **Эшелонированная Безопасность (Defense-in-Depth MCP):** Все MCP-коммуникации проходят через многоуровневую систему защиты.
- **Самоисправление (Self-Correction):** Каждый production-агент реализует цикл Plan → Act → Reflect → Revise.
- **Compile-Time RAG:** Синтез знаний перенесён из времени запроса во время ингеста, что снижает затраты на токены на 90%.

---

## 🧠 Новые возможности (v13.01)

### Самоисправляющиеся агенты
ARIA реализует цикл Plan → Act → Reflect → Revise:
- **OdabNote** — иммунная система: сохраняет паттерны ошибок и решения
- **Vibe Check** — предотвращает перепроектирование и уход от задачи
- **Reflection Loop** — автоматическая коррекция параметров и повтор при сбоях

### Compile-Time RAG
- **Knowledge Compiler** компилирует сырые данные в структурированную вики
- Затраты на токены снижены на 90%, задержка — с 2-5 секунд до <100 мс

### Промышленная надёжность
- **AI‑DLQ Handler** — автоматическая обработка Dead Letter Queue через LLM
- **Failure Clustering** — группировка сбоев по первопричине (DBSCAN)
- **Flaky Detector** — обнаружение нестабильности стратегий

### Безопасность цепочки поставок
- **Pre‑Commit Secret Scanner** — блокировка коммитов с приватными ключами
- **External Link Integrity Monitor** — периодическая проверка внешних ссылок
- **Token Security Scanner** — проверка токенов перед взаимодействием

---

## 🚀 Интегрированные Технологии и Платформы

### 🧠 Мозг и Мышление
- **Рассуждение и Планирование:** `GLM‑5.1`, `MiniMax‑M27`, `Qwen3.6‑27B`, `DeepSeek‑V3`, `Trinity Reasoning Engine`, `Quest`, `CoRT`, `LEAD`, `Think‑with‑Rubrics`
- **Верификация:** `EBM Engine`, `Bias Firewall`, `Context7`, `NotebookLM MCP`, `GitMCP`, `VAC`

### 📊 Данные и Аналитика
- **RAG и Память:** `RAGFlow (DeepDoc)`, `Cognee`, `Graphiti`, `Trieve`, `LanceDB`, `AssistRAG`, `StreamingRAG`
- **Поиск:** `Firecrawl MCP`, `Exa MCP`, `Perplexity MCP`, `Trafilatura`, `GPT Researcher`, `TrendRadar`, `Notte`

### 💹 Финансовые Данные и Трейдинг
- **Фундаментальные данные:** `Alpha Vantage MCP`
- **Крипто-шлюз:** `CCXT MCP Server` (100+ бирж)
- **Технический анализ:** `TradingView MCP`
- **Ончейн-разведка:** `Arkham Intel`
- **Риск-менеджмент:** `MonteWalk`, `RL-CVaR`

### 🤖 Автономное Кодирование и Оркестрация
- **Само-модификация:** `MOSS`, `RESD`, `DeltaBox`
- **Оркестрация:** `Shrimp Task Manager`, `Dagu`, `WorkflowGen`
- **CI/CD:** `Microsandbox`, `Dagger`, `Trigger.dev`

### 🔒 Безопасность
- **Шлюзы:** `mcp-proxy`, `ACO Prompt Shield`, `GuardRAG`
- **Аудит:** `MCP Audit`, `CacheRact`
- **Мониторинг:** `Grafana MCP`, `Prometheus MCP`, `Agent-ToM`
- **Threat Intelligence:** `FastMCP ThreatIntel`, `CrowdStrike Falcon MCP`

---

## 📚 Документация

- **[AXIOMS.md](./AXIOMS.md)** — Полный перечень 420 аксиом
- **[SKILLS.md](./SKILLS.md)** — Каталог 130+ навыков агентов
- **[INTEGRATIONS.md](./INTEGRATIONS.md)** — Реестр MCP-серверов и технологий
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** — Детальная архитектура контуров
- **[SECURITY.md](./SECURITY.md)** — Политика безопасности
- **[ROADMAP.md](./ROADMAP.md)** — План развития до v14.00
- **[TRAINING_LOG.md](./TRAINING_LOG.md)** — Хронология обучения
- **[docs/REFERENCES.md](./docs/REFERENCES.md)** — Библиография

---

**ARIA + Игорь = Бесконечное Совершенствование. Навсегда.**
