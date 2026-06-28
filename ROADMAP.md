# ROADMAP.md — План развития ARIA AI‑Factory

## v13.01 (текущая) — "Готовность к запуску"
- ✅ Создание и консолидация инфраструктуры знаний (CHANGELOG, INTEGRATIONS, TRAINING_LOG, SECURITY, BOOTSTRAP)
- ✅ Аудит и синхронизация репозитория
- ✅ Обновление AXIOMS.md до 420 аксиом
- ✅ Интеграция Self‑Correcting Agents (OdabNote, Vibe Check, Reflection Loop)
- ✅ Интеграция Compile‑Time RAG (Knowledge Compiler)
- ✅ Интеграция Decaying Episodic Memory (Max Planck Institute)
- ✅ Интеграция AI‑DLQ Handler
- ✅ Интеграция Failure Clustering и Flaky Detector
- ✅ Интеграция Pre‑Commit Secret Scanner и CI/CD Security Pipeline
- ✅ Интеграция External Link Integrity Monitor
- ✅ Интеграция Token Security Scanner
- ✅ Проект «Охотник 6.0» (Options Trading): полностью автономная система арбитража волатильности
- ✅ Обновление ARCHITECTURE.md (Compile‑Time RAG, Architectural Compliance, Self‑Correcting Agents)
- ✅ Обновление SECURITY.md (Self‑Correction, Supply Chain Security, Failure Monitoring)
- ✅ Обновление README.md до v13.01 с описанием всех новых возможностей
- 🔧 Ожидание IP-адреса боевого сервера
- 🔧 Развёртывание через docker compose

## v13.02 — "Интеллектуальная разведка и консолидация"
**Цель**: Подключение приоритетных интеграций, завершение консолидации, усиление безопасности

**Финансовый контур**:
- Alpha Vantage MCP Server (официальный) — приоритетная интеграция
- CCXT MCP Server (jcwleo) — приоритетная интеграция
- QuantDinger — ожидает конфигурации
- TradingView MCP — ожидает конфигурации
- Financial Datasets MCP — дополнительный источник данных

**Веб-разведка и OSINT**:
- BrightData MCP — резервный канал
- Notte — основной фреймворк для сложной веб-разведки
- Perplexity MCP — оперативный поиск (опционально)
- ArXiv MCP Server — запланирован

**Безопасность**:
- MCP Audit — приоритетная интеграция
- MalwarePT — приоритетная интеграция (бинарный сканер)
- Anthropic Cybersecurity Skills — референсная библиотека
- Интеграция `claude-cowork-prompt-injection` в CI/CD — срочная мера по защите от Prompt Injection
- Интеграция `mcp-security-tools` (Unit 42) и `prompt-guard` (GitHub) — приоритетная интеграция
- Интеграция `ACO Prompt Shield` как активного фильтра MCP-трафика — приоритетная интеграция
- Приведение безопасности MCP в соответствие со стандартами Elastic, OWASP и Microsoft — срочная архитектурная задача

**Инфраструктура и CI/CD**:
- IBM ContextForge — приоритетная интеграция
- Metorial — приоритетная интеграция
- MetaMCP — приоритетная интеграция
- mcp-proxy — приоритетная интеграция (усиление функциями Request/Response Inspection, Tool Name Allow-listing, Schema Validation)
- IBM MCP CLI — приоритетная интеграция
- GenAIScript — приоритетная интеграция
- Archestra — приоритетная интеграция
- Refact — приоритетная интеграция
- SocratiCode — приоритетная интеграция (замена Sourcebot)
- Shrimp Task Manager — приоритетная интеграция (когнитивный планировщик)
- MCP Router — приоритетная интеграция (визуальная панель управления)
- Dagu — приоритетная интеграция (оркестрация рабочих процессов)
- lean-ctx — приоритетная интеграция
- Unla — приоритетная интеграция (замена Higress)
- DeltaBox — приоритетная интеграция (мгновенные чекпоинты, интеграция с MOSS)
- Solon — запланирован для некритических серверов

**Память и исследования**:
- PapersGPT for Zotero — приоритетная интеграция
- Quest — приоритетная интеграция (основной движок разведки)
- MarkItDown — приоритетная интеграция
- Graphify — приоритетная интеграция
- CoRT — приоритетная интеграция (мета-когнитивный движок)
- ByteRover CLI — приоритетная интеграция
- Pezzo — запланирован
- Basic Memory — запланирован

**HITL и коммуникации**:
- Google Workspace MCP — приоритетная интеграция (замена notebooklm-mcp)
- MCP Agent Mail — приоритетная интеграция
- PromptX — приоритетная интеграция
- n8n-nodes-mcp — приоритетная интеграция
- Vexa AI — тестирование голосового HITL

**Базы данных**:
- DBHub — приоритетная интеграция
- Postgres MCP (Crystal DBA) — запланирован
- MCP Server PostgreSQL/MySQL/SQL Server — запланирован (дополнение к DBHub)

**Наблюдаемость**:
- Grafana MCP — приоритетная интеграция
- Prometheus MCP — приоритетная интеграция

**Научные работы**:
- Beyond the Hype (AgentEval Suite + AgentSandbox) — приоритетная интеграция
- Quest — приоритетная интеграция
- DeltaBox — приоритетная интеграция
- Graph-RAG for Codebases — научное обоснование выбора SocratiCode

**Безопасность (срочные меры)**:
- Sandboxed-тестирование MCP-серверов
- Lockfile enforcement (`npm ci`)
- Аудит установленных MCP-серверов
- Загрузка IoC из статей по безопасности
- Внедрение Suricata-сигнатур
- Аудит экспозиции MCP-серверов (Shodan/Censys)
- Обязательная аутентификация на всех MCP-серверах
- Ограничение capabilities (sampling, roots)
- Внедрение AGENTS.md + GitHub Action для фильтрации AI‑генерированных PR
- Внедрение эшелонированной защиты MCP (Zero Trust, валидация, санитизация)
- Интеграция `claude-cowork-prompt-injection` и `mcp-security-tools` в CI/CD
- Развёртывание `ACO Prompt Shield` в `mcp-proxy`

## v13.03 — "Первая операционная прибыль"
**Цель**: Активация Self-Modification Engine, полный цикл автономной разработки, первая сделка

**Развёртывание и запуск**:
- Развёртывание на боевом сервере
- Подключение к биржам через CCXT MCP Server и Arkham Intel
- Запуск Фазы Тишины (пассивное наблюдение)
- Первая HITL‑подтверждённая сделка (0.1% депозита)

**Self-Modification Engine**:
- MOSS — замена текущего Self-Modification Engine
- RESD — основной RL-фреймворк (замена Memory-R2 + Selective Hindsight Distillation)
- SkillEvolBench — бенчмарк для валидации навыков
- Skills on the Fly — временные навыки для быстрой адаптации

**Торговля и прогнозирование**:
- Dynamic TMoE — адаптивный прогноз
- L-Drive — латентный контекст
- ECM — пост-процессинг прогнозов
- Alpha Factor Discovery RL — RL для альфа-факторов
- FinCAD — debiasing стратегий
- MonteWalk — симуляции Монте-Карло и стресс-тестинг

**Исследования**:
- Argus — надстройка над Quest для эффективного deep research
- OnePred — предиктор следующего запроса для HITL
- Self-Improving ICL — мгновенная адаптация промптов
- GoLongRL — рецепт пост-тренировки для Quest
- CoMERA-Agent — аппаратно-осознанное сжатие контекста (опционально)

**Безопасность**:
- CrowdStrike Falcon MCP — интеграция (после стабилизации)
- FastMCP ThreatIntel — приоритетная интеграция (замена IoC Research MCP)
- MemRepair — авто-ремонт уязвимостей с MOSS
- Contextual Integrity — безопасность LLM
- Wazuh IOC Hunter MCP — опционально
- Адаптация Anthropic Cybersecurity Skills в GenAIScript-инструменты
- Интеграция `CacheRact` как Red Team инструмента для тестирования безопасности KV-кэша

**OSINT и Threat Intelligence**:
- frishtik/osint-tools-mcp-server — основной OSINT-агрегатор
- OSINT Tools MCP, OSINT Toolkit MCP, Sycek MCP (платный), MetaOSINT
- Dork MCP, Uncurl MCP, Spider MCP, CyberChef MCP, GreyNoise MCP

**Инфраструктура**:
- TOAP — Tool Preference Learner для MetaMCP
- Contexting as Recommendation — эволюционный подбор контекста
- PEEK — ориентационный кэш для длинных контекстов
- Context Pruning — обрезка контекста для coding-агентов
- Nudging Exploration — улучшение exploration в RLVR
- Microservices Root Cause — локализация сбоев
- Dev Containers CLI — воспроизводимые среды разработки
- GROW — RL для VLM-агентов
- Supabase MCP — управление платформой
- Trieve — единая retrieval-инфраструктура (замена LanceDB, Cognee, Graphiti)
- Fusio — стандартизация REST API (опционально)

**Память и знания**:
- AssistRAG — проактивное управление памятью
- GuardRAG — защита RAG от Prompt Injection
- TTCO (Test-Time Critique and Optimization) — улучшение retrieval через критику на инференсе
- StreamingRAG — потоковый retrieval для real-time данных (интеграция с Trieve и Alpha Vantage MCP)
- GraphIC — графовое In-Context Learning для усиления KumoRFM‑2

**Визуализация и HITL**:
- VAC — верификация визуальных отчётов
- Peekaboo — захват экрана
- Vexa AI — целевая интеграция голосового HITL

**GUI-стек (базовый уровень)**:
- CogAgent — визуальное восприятие GUI (MCP-сервер)
- GUI‑R1 — reasoning для GUI-задач
- UI‑Copilot — управление памятью и контекстом (замена SE‑GA)
- UFO — архитектура HostAgent → AppAgent (референсная модель)
- WebVoyager — MCP-инструмент для веб-навигации

**Научные работы и бенчмарки**:
- SkillEvolBench — валидация Self-Modification Engine
- RoleMemo (из DUALMEM) — бенчмарк для оценки памяти
- TradingBench — основной бенчмарк для оценки финансовых агентов (интеграция с AgentEval Suite)
- Agent Reward Benchmark — полигон для динамического тестирования агентов
- WebWalker — бенчмарк для оценки веб-навигации Quest и Notte
- ICL Under Regime Change — теоретический фундамент для адаптации к смене рыночных режимов

**Мониторинг и оптимизация**:
- Непрерывный аудит производительности через Grafana MCP
- Мониторинг задержек и затрат токенов

## v14.00 — "Квантовый хаб и полная автономия"
**Цель**: Активация Квантового Хаба, полная мульти-модельная архитектура, расширенная автономия

**Квантовые вычисления**:
- Quantum End-to-End Learning — практический квантовый оптимизатор
- Подключение к IBM Quantum, AWS Braket

**Риск-менеджмент**:
- RL-CVaR — динамический риск-менеджмент

**Мульти-модельная архитектура**:
- Tensor Cache — двухуровневый кэш для LLM
- Latent Cache Flow — мульти-модельная коммуникация
- DUALMEM — обучение собственной персонифицированной модели памяти
- Agent-ToM — мониторинг безопасности автономных агентов (усиление защитой от манипуляции и непроизвольного ICL)

**Инфраструктура и разработка**:
- Solon — для критических Java-серверов
- CoplayDev Unity MCP — основной 3D-движок
- Design Extract — визуальный аудит и генерация UI
- Multica — панель управления AI-командой
- Fusio — полная интеграция
- Py-xiaozhi — edge/IoT-голос

**GUI-стек (продвинутый уровень)**:
- Mobile-Agent — надёжное выполнение и рефлексия для GUI
- EchoTrail-GUI — межсессионное накопление GUI-опыта
- PV-UFO — параллельное выполнение GUI-задач
- AppAgent — автономное исследование приложений (паттерн Exploration)
- UFO — полная интеграция как основного GUI-фреймворка

**OSINT (продвинутые)**:
- SocNetEcho MCP, Recorded Future MCP, Censys MCP, CriminalIP MCP
- Sherlock MCP, Holehe MCP, Blackbird MCP, Photon MCP

**HITL и коммуникации**:
- Apple MCP (griches) — нативные приложения macOS
- Home Assistant MCP — умное окружение
- TriliumNext Notes — HITL-инструмент для графа знаний
- slackdump — сбор данных из Slack-сообществ
- md2wechat-skill — конвертация отчётов в WeChat
- iOS Simulator MCP — управление iOS-симулятором

**Безопасность (стратегический уровень)**:
- Involuntary ICL — защита от непроизвольного обхода safety alignment
- Exploration Hacking awareness — учёт при проектировании Agent‑ToM и мониторинга MOSS

**Дальнейшие планы (v14.01+)**:
- SAFEFL — федеративное обучение с privacy-preserving
- Полная автономия: HITL только для критических операций
- Мульти‑агентная экспансия на глобальной serverless‑инфраструктуре
