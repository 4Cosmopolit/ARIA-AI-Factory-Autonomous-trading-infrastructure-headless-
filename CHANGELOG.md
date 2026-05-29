# CHANGELOG.md — История версий ARIA AI‑Factory

## v13.01 (Июнь 2026) — "Готовность к запуску"
### 🔧 Финальная синхронизация
- Устранены расхождения между документацией, `TRAINING_LOG.md` и фактическим состоянием репозитория.
- Создан `CHANGELOG.md` (этот файл) для сохранения полной истории изменений.
- Проведён аудит всех 110+ записей из `TRAINING_LOG.md`; ключевые инструменты перенесены в `INTEGRATIONS.md`.
- Актуализирован `SKILLS.md` с учётом новейших изученных технологий.

### 🚢 Подготовка к деплою
- Ожидание IP-адреса боевого сервера.
- Сформирована команда развёртывания (`docker compose -f docker-compose.v13.yml up -d`).
- План `BOOTSTRAP.md` полностью готов к исполнению.
- Цель: первая операционная прибыль в версии **v13.03**.

### 📄 Инфраструктура знаний
- Завершено создание ключевых документов: `BOOTSTRAP.md`, `CONTINUITY.md`, `TRAINING_LOG.md`, `SECURITY.md`, `INTEGRATIONS.md`, `CHANGELOG.md`.
- Аксиомы (`AXIOMS.md`) актуализированы (343 аксиомы).
- Архитектура (`ARCHITECTURE.md`) отражает 7 контуров и 4 сверх-ядра.

### 🔄 Ключевые архитектурные замены (9)
- Sourcebot → **SocratiCode**
- Godot MCP + IvanMurzak/Unity‑MCP → **CoplayDev/unity‑mcp**
- Browserbase MCP → **BrightData MCP** → **Notte**
- Zotero MCP → **PapersGPT for Zotero**
- notebooklm‑mcp → **Google Workspace MCP**
- Higress → **Unla**
- Financial Datasets MCP → **Alpha Vantage MCP (официальный)**
- GOAT → **Arkham Intel**
- Memory‑R2 + Selective Hindsight Distillation → **RESD**

### 🛡️ Безопасность MCP (новый стандарт)
- Приняты стандарты безопасности: OWASP MCP Tool Poisoning, Unit 42 (Palo Alto Networks), Elastic Security Labs, Tenable, Netskope, GitHub Security Lab, Practical DevSecOps.
- Внедрены инструменты защиты: `mcp-proxy`, `ACO Prompt Shield`, `prompt-guard`, `claude-cowork-prompt-injection`.
- Реализована политика Total Zero Trust для всех MCP-взаимодействий.
- Добавлены кейсы реальных инцидентов: Microsoft Copilot exfiltration (PromptArmor), Google AntiGravity exfiltration (PromptArmor).
- Принята концепция «Нормализации девиантности» (Embrace The Red) как культурный принцип безопасности.

### 🖥️ GUI-стек (полный цикл)
- CogAgent (CVPR 2024) — визуальное восприятие.
- GUI‑R1 — reasoning‑first подход к GUI-задачам.
- UI‑Copilot (Memory Decoupling + TIPO) — управление памятью и контекстом.
- UFO (Microsoft) — HostAgent → AppAgent архитектура.
- PV‑UFO — параллельное выполнение GUI-задач.
- Mobile‑Agent — надёжное выполнение с рефлексией.
- EchoTrail‑GUI — межсессионное накопление GUI-опыта.
- AppAgent — автономное исследование приложений.
- OS‑Copilot (FRIDAY) — саморазвивающийся агент (референс).

---

## v12.95 (Июнь 2026) — "Консолидация и Знание"
### 🧬 Архитектурная консолидация
- Полная реструктуризация 70+ MCP‑серверов в **4 сверх‑ядра**:
  - `Aria‑Cognitive‑Core`
  - `Aria‑Memory‑Core`
  - `Aria‑Sentinel‑Core`
  - `Aria‑Interface‑Hub`
- Устранение дублирующих компонентов, устаревшего кода и неиспользуемых зависимостей.

### 🚀 Новые интеграции (110+ изучено, 60+ одобрено)
- **Финансы:** GOAT (единый on‑chain уровень), QuantDinger.
- **AI‑шлюзы и маршрутизация:** Bifrost (50x быстрее LiteLLM), vLLM Semantic Router, Higress, Klavis AI.
- **Оркестрация:** fast‑agent, Langroid, mcp‑agent, PraisonAI, Swarms (kyegomez), Cyrus Agents, Agent Swarm Resilience, Genkit, Lemonade, AutoAgent, Ruflo.
- **Визуализация и интерфейсы:** PPTAgent, AntV MCP, Excalidraw MCP, Magic MCP, CopilotKit, Excel MCP, RealChar, Open WebUI, Draw.io AI Diagram.
- **3D‑моделирование и симуляции:** FreeCAD MCP, Godot MCP, BlenderMCP.
- **Безопасность:** VIPER, MISP, HexStrike, Ghidra MCP + IDA Pro MCP, Agentic Radar, ENScan_GO, `aidefence` (Content Security Pipeline), Microsandbox (аппаратная изоляция KVM).
- **Инфраструктура и CI/CD:** Dagger Container Use, Cloudflare MCP, GitHub MCP, Spec Workflow MCP, Task Master, kubefwd, Docker, Self‑Modification Engine.
- **Веб‑разведка:** Firecrawl MCP, Exa MCP, U14 Deep Research, Trafilatura, YouTube Transcript API, Xiaohongshu MCP, TrendRadar, GPT Researcher.
- **RAG и память:** RAGFlow (DeepDoc), Cognee (ECL‑конвейер), Airweave, UltraRAG, NotebookLM MCP (дважды), Context7, GitMCP, Graphiti, Beads, LanceDB, GreptimeDB, SEmble, OpenMetadata.
- **Коммуникации:** Fonoster, WhatsApp MCP, OpenClaw, Telegram MCP.
- **Локальный AI:** Ollama, Hermes Agent.
- **HITL и обратная связь:** `mcp-feedback-enhanced` (одобрен, ожидает конфигурации для Фазы 1).
- **Терминальные агенты:** Gemini CLI, Codex CLI.
- **Песочницы:** Code Interpreter API, HttpRunner.

### 🛡️ Безопасность и отказоустойчивость
- Внедрение трёхступенчатого Content Security Pipeline (`aidefence`).
- Аппаратная изоляция критических компонентов через Microsandbox (KVM).
- Извлечены уроки из CVE‑2025‑68143/68144 (Notion MCP).
- Задокументирован инцидент Polymarket (Admin Key Security).
- Политика Zero Trust распространена на все новые MCP‑серверы.

### 📚 Документация и обучаемость
- Создан `TRAINING_LOG.md` с хронологией изучения 110+ инструментов и их привязкой к аксиомам.
- Подготовлены `INTEGRATIONS.md` (реестр одобренных компонентов) и `SECURITY.md`.
- Обновлён `SKILLS.md` (более 100 активных навыков).
- Проведён полный аудит репозитория, все знания перенесены из чатов в GitHub.

---

## v12.06–v12.92 (Май–Июнь 2026) — "Эра Агентной Инженерии"
### 🧠 Агентная инженерия
- Внедрение Agentic Engineering (LangChain, Augment Code, Superpowers, OpenSpec).
- Интеграция Claude Code Swarm, OpenClaw, Swarms.ai, Ruflo, Agent Swarm Resilience.
- Внедрение Blind Review Gate и Anti‑Sycophancy Check для всех стратегий.
- Запуск автономной само‑модификации кода (`self‑modification‑engine`).

### 📊 Retrieval и память
- Интеграция Context7, NotebookLM MCP (первое поколение), GitMCP.
- Внедрение семантического кэширования (Claude Context, Zilliz).
- Подключение RAGFlow (DeepDoc), Cognee (ECL‑конвейер), Airweave.

### 🔒 Безопасность
- Внедрение Agentic Radar (SAST/DAST для агентов).
- Интеграция HexStrike (аудит смарт‑контрактов).
- Анализ и устранение уязвимости BrowserTools MCP (CVE‑2026‑7064).

### 🎨 HITL и визуализация
- Интеграция Dify, LangFlow, n8n.
- Внедрение Excalidraw MCP, AntV MCP, PPTAgent.
- Подключение CopilotKit для интерактивных AI‑интерфейсов.

### 🤖 Агентная оркестрация
- Интеграция fast‑agent, Langroid, mcp‑agent, PraisonAI.
- Переход на Actor‑модель обмена сообщениями между компонентами.

---

## v11.01–v12.05 (Май 2026) — "Фундамент"
- Создана первоначальная архитектура ARIA AI‑Factory.
- Интеграция базовых LLM‑моделей: DeepSeek‑V3, Gemini CLI, Codex CLI.
- Внедрение протоколов TradeMemory, OpenSpec, Superpowers.
- Заложены основы аксиоматики и реестра навыков.
- Начало формирования Agentic Engineering как методологии.
