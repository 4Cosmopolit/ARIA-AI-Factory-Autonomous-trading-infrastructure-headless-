# CHANGELOG.md — История версий ARIA AI‑Factory

## v13.01 (Июнь 2026) — "Сингулярность"

### 🧬 Архитектурная консолидация
- Полная реструктуризация MCP-серверов в 4 сверх-ядра: `Aria‑Cognitive‑Core`, `Aria‑Memory‑Core`, `Aria‑Sentinel‑Core`, `Aria‑Interface‑Hub`.
- Устранение дублирующихся компонентов и устаревшего кода.

### 🚀 Новые интеграции (40+ MCP-серверов)
- **Финансы:** GOAT (единый on‑chain уровень), QuantDinger.
- **AI‑шлюзы:** Bifrost (50x быстрее LiteLLM), vLLM Semantic Router, Higress.
- **Оркестрация:** fast‑agent, Langroid, mcp‑agent, PraisonAI, Genkit, Lemonade.
- **Визуализация:** PPTAgent, AntV, Excalidraw, Magic MCP, CopilotKit, Excel MCP.
- **Безопасность:** VIPER, MISP, HexStrike, Ghidra MCP + IDA Pro MCP, Agentic Radar, ENScan_GO.
- **Инфраструктура:** Microsandbox, Dagger, Cloudflare MCP, GitHub MCP, Spec Workflow MCP, Task Master, kubefwd.
- **Веб‑разведка:** Firecrawl MCP, Exa MCP, U14 Deep Research, Trafilatura, YouTube Transcript API, Xiaohongshu MCP, TrendRadar, GPT Researcher.
- **RAG и память:** RAGFlow, Cognee, Airweave, UltraRAG, NotebookLM MCP, Context7, GitMCP, Graphiti, Beads, LanceDB, GreptimeDB, SEmble, OpenMetadata.
- **3D‑моделирование:** FreeCAD MCP, Godot MCP, BlenderMCP.
- **Коммуникации:** Fonoster, WhatsApp MCP, OpenClaw, Open WebUI, RealChar.
- **Локальный AI:** Ollama, Hermes Agent.
- **Терминальные агенты:** Gemini CLI, Codex CLI.
- **Песочницы:** Code Interpreter API, HttpRunner.

### 🛡️ Безопасность и отказоустойчивость
- Внедрение `aidefence` — трёхступенчатого Content Security Pipeline.
- Интеграция `Microsandbox` для аппаратной изоляции (KVM).
- Уроки безопасности из CVE‑2025‑68143/68144 (Notion MCP).
- Уроки безопасности из инцидента Polymarket (Admin Key Security).

### 📚 Документация
- Перенос всех знаний из чата в репозиторий GitHub.
- Создание `AXIOMS.md` (343 аксиомы), `SKILLS.md` (100+ навыков), `ARCHITECTURE.md`.

---

## v12.06–v12.92 (Май–Июнь 2026) — "Эра Агентной Инженерии"

### 🧠 Агентная инженерия
- Внедрение Agentic Engineering (LangChain, Augment Code, Superpowers, OpenSpec).
- Интеграция Claude Code Swarm, OpenClaw, Swarms.ai, Ruflo, Agent Swarm Resilience.
- Внедрение Blind Review Gate и Anti‑Sycophancy Check.
- Автономная само‑модификация кода (`self‑modification‑engine`).

### 📊 Retrieval и память
- Интеграция Context7, NotebookLM MCP, GitMCP.
- Внедрение семантического кэширования (Claude Context).
- Интеграция RAGFlow (DeepDoc), Cognee (ECL‑конвейер), Airweave.

### 🔒 Безопасность
- Внедрение Agentic Radar (SAST/DAST для агентов).
- Интеграция HexStrike (аудит смарт‑контрактов).
- Уроки безопасности из BrowserTools MCP (CVE‑2026‑7064).

### 🎨 HITL и визуализация
- Интеграция Dify, LangFlow, n8n.
- Внедрение Excalidraw MCP, AntV MCP, PPTAgent.
- Интеграция CopilotKit для интерактивных AI‑интерфейсов.

### 🤖 Агентная оркестрация
- Интеграция fast‑agent, Langroid, mcp‑agent, PraisonAI.
- Внедрение Actor‑модели обмена сообщениями.

---

## v11.01–v12.05 (Май 2026) — "Фундамент"

- Первоначальная архитектура ARIA AI‑Factory.
- Интеграция DeepSeek‑V3, Gemini CLI, Codex CLI.
- Внедрение TradeMemory Protocol, OpenSpec, Superpowers.
- Базовые навыки и аксиомы.
