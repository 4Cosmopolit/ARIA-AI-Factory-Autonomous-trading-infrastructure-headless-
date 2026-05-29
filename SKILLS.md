# SKILLS.md — Реестр навыков ARIA AI‑Factory v13.01 (обновлён 29.05.2026)

## Категория 1: Качество данных (Data Quality)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| data-contract-validator | L2 | Валидация данных по формальным контрактам (единицы, диапазоны, контекст). | ARIA Core |
| self-describing-data | L2 | Автоматическая семантическая аннотация каждого факта в Temporal KG. | ARIA Core |
| signal-augmentation-engine | L2 | Обогащение сигналов вычисляемыми полями (прогноз волатильности, рейтинг безопасности хуков). | ARIA Core |
| lineage-tracer | L2 | Отслеживание происхождения каждого факта (полная карта provenance). | ARIA Core |
| impact-analyzer | L2 | Анализ влияния изменений в данных на стратегии и агентов. | ARIA Core |
| compliance-verifier | L2 | Автоматическая подготовка доказательной базы для аудита (GDPR, AI Act). | ARIA Core |
| realism-validator | L2 | Проверка синтетических данных на соответствие реальным паттернам. | ARIA Core |
| data-debt-detector | L2 | Мониторинг накопления «долгов» по качеству данных (confidence, просрочка). | ARIA Core |
| extractor-framework | L1 | Компонуемые экстракторы для разных типов данных с однопроходным обходом (Figma-Context-MCP). | ARIA Core |
| deepdoc-parser | L2 | Глубокое понимание документов (92% точность, 12 форматов). | RAGFlow |
| ragognizer-hallucination-detection | L2 | Проактивная детекция галлюцинаций на уровне токенов через встроенную detection head | RAGognizer |

## Категория 2: Безопасность и изоляция (Security & Isolation)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| aria-gov-gateway | L1 | Единый шлюз безопасности с deny-first политикой. | ARIA Core |
| permissions-drift-detector | L2 | Контроль расширения прав навыков при обновлении. | ARIA Core |
| trust-chain-validator | L2 | Верификация цепочки доверия (агент → навык → зависимости). | ARIA Core |
| model-integrity-checker | L2 | Проверка целостности весов и кода моделей в памяти. | ARIA Core |
| bitflip-detector | L2 | Детектор битовых аномалий (Rowhammer, bit-flip атаки). | ARIA Core |
| destructive-command-detector | L1 | Блокировка деструктивных SQL/Shell команд (DROP, DELETE, rm -rf). | ARIA Core |
| lolbin-detector | L2 | Обнаружение аномального использования легитимных утилит (curl, git, ssh). | ARIA Core |
| telegram-guard | L1 | Защита от prompt injection через входящие сообщения Telegram. | ARIA Core |
| phishing-url-scanner | L2 | Сканер фишинговых URL перед переходом. | ARIA Core |
| approve-guard | L1 | HITL-подтверждение для всех approve/allowance транзакций. | ARIA Core |
| resource-abuse-detector | L2 | Детектор аномального потребления CPU/RAM/сети в sandbox. | ARIA Core |
| harness-firewall | L1 | Второй HITL-фильтр для изменений в конфигурациях обвязки. | ARIA Core |
| prompt-version-lock | L1 | Версионирование системных инструкций с хеш-контролем. | ARIA Core |
| aidefence-pipeline | L1 | Трёхступенчатый Content Security Pipeline (pre‑check, process‑check, post‑check). | Ruflo |
| agentic-sast | L2 | Статический анализ агентных рабочих процессов (SAST). | Agentic Radar |
| agentic-dast | L2 | Динамическое тестирование агентов (Prompt Injection, PII Leakage). | Agentic Radar |
| prompt-hardening | L2 | Автоматическая закалка промптов (OWASP LLM Top 10). | Agentic Radar |
| smart-contract-audit | L2 | Аудит смарт-контрактов перед взаимодействием (HexStrike). | HexStrike |
| threat-intel-lookup | L2 | Проверка адресов/транзакций по глобальной базе угроз (MISP). | MISP |
| red-team-automation | L2 | Автономная имитация атак (VIPER, 100+ модулей MITRE ATT&CK). | VIPER |
| binary-analysis | L2 | Реверс-инжиниринг бинарного кода (Ghidra + IDA Pro). | GhidraMCP |
| china-osint | L2 | OSINT по китайским юридическим лицам (ENScan_GO). | ENScan_GO |
| microsandbox-isolation | L1 | Аппаратно-изолированные песочницы (KVM, запуск <100ms, MCP-сервер). | Microsandbox |
| falcon-mcp-security-orchestrator | L2 | Управление безопасностью через CrowdStrike Falcon (EDR, Threat Intel, реагирование) | CrowdStrike Falcon MCP |
| wazuh-ioc-hunter | L2 | Обогащение IOC из алертов Wazuh | Wazuh IOC Hunter MCP |
| malwarept-binary-screening | L2 | Автоматический бинарный скрининг всех артефактов ARIA | MalwarePT |
| jadx-android-reversing | L2 | Специализированный реверс-инжиниринг Android-приложений | JADX AI MCP |
| mcp-proxy-gateway | L2 | Управление пограничным шлюзом безопасности MCP с функциями валидации, allow-listing и санитизации | mcp-proxy |
| cort-recursive-thinking | L2 | Рекурсивное мета-когнитивное мышление для улучшения ответов | CoRT MCP |
| agent-tom-monitoring | L2 | Мониторинг автономных агентов через Theory-of-Mind, включая детекцию манипуляции и эскалации привилегий | Agent-ToM |
| resd-failure-learning | L2 | Обучение на неудачах через Reflection-Enhanced Self-Distillation | RESD |
| guardrag-injection-defense | L2 | Двухуровневая защита RAG от prompt injection: Knowledge Base Firewall + Response-Level Agent | GuardRAG |
| aco-prompt-shield | L2 | Активный MCP-сервер фильтрации: детекция инъекций, PII-валидация, санитизация ввода/вывода | ACO Prompt Shield |
| prompt-guard-client | L2 | Клиентская защита MCP: автоматическое экранирование и визуальное выделение данных от серверов | prompt-guard (GitHub) |
| mcp-security-audit | L2 | Комплексный аудит безопасности MCP-серверов согласно стандартам OWASP, Unit 42, Elastic | MCP Audit |
| cacheract-red-team | L2 | Red Team тестирование уязвимости KV-кэша для эксфильтрации данных | CacheRact |
| proteus-adaptive-red-team | L2 | Самоэволюционирующая красная команда для тестирования навыков и MCP-серверов | Proteus |
| behavioral-canaries-audit | L2 | Аудит приватности RL-обучения через внедрение canary-примеров | Behavioral Canaries |
| code-whisperer-graph-repair | L2 | Комплексный анализ и исправление уязвимостей через графовый анализ + LLM | The Code Whisperer |
| vultriage-vulnerability-detection | L2 | Тройная контекстная аугментация для детекции уязвимостей в коде | VulTriage |

## Категория 3: Управление контекстом и памятью (Context & Memory)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| compress-context | L1 | Авто-сжатие контекста при занятости >70% окна. | ARIA Core |
| context-length-monitor | L1 | Принудительное сжатие входящего контекста при превышении лимита. | ARIA Core |
| auto-memory-audit | L2 | Ежедневный аудит памяти: дубликаты, устаревшие факты, галлюцинации. | ARIA Core |
| context-integrity-daemon | L1 | Фоновая проверка целостности ключевых параметров сессии. | ARIA Core |
| context-access-simulator | L2 | Симуляция атаки на утечку контекста в sandbox. | ARIA Core |
| viral-context-injector | L2 | Вшивание мета-принципов (честность, сжатие, приоритеты) в начало сессии. | ARIA Core |
| context-mode-think-in-code | L1 | Think-in-Code парадигма: экономия контекста до 98%. | Context Mode |
| semantic-caching | L2 | Семантическое кэширование (10x‑100x ускорение retrieval). | Claude Context |
| graphiti-dynamic-kg | L2 | Динамический темпоральный граф знаний с автоматическим разрешением противоречий. | Graphiti |
| cognee-ecl-pipeline | L2 | ECL‑конвейер (Extract → Cognify → Load) для извлечения знаний. | Cognee |
| ragflow-deepdoc | L2 | Enterprise-grade документный парсер с гибридным retrieval. | RAGFlow |
| notebooklm-source-grounding | L2 | Source‑grounded ответы с цитатами из загруженных документов. | NotebookLM |
| gitmcp-living-docs | L2 | Мгновенный доступ к живой документации любого GitHub-проекта. | GitMCP |
| context7-verification | L1 | Проверка API-вызовов на соответствие актуальной документации. | Context7 |
| semble-compression | L2 | Сжатие эмбеддингов на 40-60% без потери точности. | SEmble |
| lance-multimodal-lake | L2 | Мультимодальное озеро данных с zero-copy передачей. | LanceDB |
| airweave-unified-search | L2 | Универсальный поиск по 50+ корпоративным источникам. | Airweave |
| lean-ctx-context-management | L2 | Оперативное управление контекстом: файлы, команды, переменные | lean-ctx |
| trieve-retrieval-platform | L2 | Единая retrieval-инфраструктура (гибридный поиск + граф знаний) | Trieve |
| graphify-knowledge-graph | L2 | Построение графа знаний из любой папки (код, документы, медиа) | Graphify |
| byterover-context-curation | L2 | Курирование и версионирование контекстных деревьев | ByteRover CLI |
| pezzo-prompt-ops | L2 | Управление жизненным циклом промптов и анализ затрат на LLM | Pezzo |
| memq-provenance-learning | L2 | Кредитное распределение через TD(λ) по provenance DAG воспоминаний | MemQ |
| hela-mem-associative | L2 | Ассоциативная память на основе хеббовского обучения | HeLa-Mem |
| two-stage-memory | L2 | Раздельная оптимизация «что сохранять» и «как использовать» воспоминания | Two-Stage Memory Optimization |
| rl-dev-memory | L2 | Специализированная память для RL-кодинг-агентов с нормализацией обратной связи | RL Developer Memory |
| dual-trace-memory | L2 | Dual-trace кодирование: сохранение фактов + «сцен» для улучшения cross-session recall | Dual-Trace Memory Encoding |
| memreranker-reasoning-retrieval | L2 | Reasoning-aware реранкинг воспоминаний через multi-stage дистилляцию | MemReranker |
| memrouter-dialogue-filter | L2 | Легковесная маршрутизация памяти (12M) для фильтрации диалогов | MemRouter |
| assistrag-proactive-memory | L2 | Проактивное управление памятью: ассистент решает, что сохранять до запроса | AssistRAG |
| streamingrag-real-time-retrieval | L2 | Потоковый retrieval для real-time индексации новостей и цен | StreamingRAG |
| hilight-evidence-focus | L2 | Фокусировка внимания LLM на ключевых доказательствах через модификацию эмбеддингов | HiLight |
| prompt-dictionary-compression | L2 | Сжатие промптов без потерь через dictionary-encoding и ICL | Lossless Prompt Compression |

## Категория 4: Токен-экономия (Token Economy)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| token-aware-routing | L1 | Маршрутизация запросов к дешёвым моделям для простых задач. | ARIA Core |
| tool-limit-enforcer | L1 | Жёсткий лимит числа вызовов MCP-инструментов за сессию. | ARIA Core |
| token-auditor | L2 | Ежедневный анализ структуры затрат токенов (полезная работа vs шум). | ARIA Core |
| semantic-tool-selection | L1 | Семантический отбор инструментов (сокращение контекста на 99.1%). | vLLM Semantic Router |
| bifrost-gateway | L2 | Автоматическое переключение между провайдерами с кэшированием. | Bifrost |
| markitdown-document-conversion | L2 | Конвертация любых форматов в Markdown (экономия до 80% токенов) | MarkItDown |
| lead-length-optimization | L2 | Адаптивное сокращение длины цепочек рассуждений через length-based efficiency rewards | LEAD |
| opsd-compaction | L2 | Пост-RL компактификация рассуждений через On-Policy Self-Distillation | OPSD Compaction |
| opsdl-long-context-distillation | L2 | Самодистилляция для длинных контекстов (усиление OPSD Compaction) | OPSDL |
| constant-context-execution | L2 | Выполнение навыков с фиксированным бюджетом контекста (LoRA + state block) | Constant-Context Skills |
| budgeted-lora-skills | L2 | Динамическое бюджетирование LoRA-модулей для баланса качество/скорость | Budgeted LoRA |
| adapshot-icl-optimizer | L2 | Адаптивный Many-Shot ICL с переиспользованием KV-кэша | AdapShot |
| phase-scheduled-mas | L2 | Фазовое планирование для токен-эффективной координации мультиагентных систем | Phase-Scheduled MAS |

## Категория 5: Инженерная дисциплина (Engineering Discipline)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| constraint-first-spec-generator | L2 | Генерация спецификаций с жёсткими ограничениями (лимиты, запреты). | ARIA Core |
| spec-test-linker | L2 | Привязка каждого пункта SPEC.md к конкретному тесту. | ARIA Core |
| intent-validator | L2 | Проверка спецификаций на избыточную детализацию (намерения vs инструкции). | ARIA Core |
| sdd-compliance-check | L1 | Обязательная проверка SPEC.md на соответствие трём принципам SDD. | ARIA Core |
| bureaucracy-detector | L2 | Анализ отчётов review-mcp и judge-mcp на признаки формализма. | ARIA Core |
| test-driven-development | L1 | RED-GREEN-REFACTOR цикл (Superpowers). | Superpowers |
| writing-plans | L2 | Разбиение работы на bite‑sized задачи (2-5 минут каждая). | Superpowers |
| subagent-driven-development | L2 | Создание свежего подагента на каждую задачу с двухстадийным ревью. | Superpowers |
| blind-review-gate | L1 | Три изолированных рецензента с Anti-Sycophancy Check. | ARIA Core |
| openspec-fluid-sdd | L2 | Жидкая разработка на основе спецификаций (OpenSpec). | OpenSpec |
| spec-workflow-structured | L2 | Структурированная среда с панелью реального времени и системой утверждения. | Spec Workflow MCP |
| httprunner-testing | L2 | AI-управляемое тестирование API/UI/производительности. | HttpRunner |
| dagger-ci-cd | L2 | MCP-управление контейнерами и CI/CD. | Dagger |
| task-master | L2 | AI-управление задачами, планирование спринтов и распределение ресурсов. | Task Master |
| self-modification-engine | L2 | Автономная само‑модификация кода с тройным слепым ревью и автоматическим откатом. | Self‑Modification Engine |
| shrimp-task-planning | L2 | Когнитивное планирование задач с CoT, рефлексией и декомпозицией | Shrimp Task Manager |
| dagu-workflow-orchestration | L2 | Оркестрация рабочих процессов через Dagu (YAML, HITL, MCP) | Dagu |
| unla-mcp-gateway-management | L2 | Zero-code конвертация REST/gRPC/WebSocket в MCP | Unla |
| metamcp-client-unification | L2 | Унификация MCP-подключений и динамическое управление инструментами | MetaMCP |
| genaiscript-prompt-engineering | L2 | Программная сборка промптов, тестирование и развёртывание AI-скриптов | GenAIScript |
| solon-mcp-development | L2 | Создание легковесных Java MCP-серверов на Solon | Solon |
| archestra-ide-mastery | L2 | AI-Native IDE для создания, тестирования и развёртывания агентов | Archestra |
| refact-agent-development | L2 | Автономная разработка кода через Refact (SWE-bench лидер) | Refact |
| socraticode-codebase-intelligence | L2 | Интеллектуальный анализ кодовой базы (гибридный поиск, impact analysis) | SocratiCode |
| ibm-mcp-cli-orchestration | L2 | Оркестрация MCP через эталонный CLI от IBM | IBM MCP CLI |
| mcp-router-visual-management | L2 | Визуальное управление MCP-инфраструктурой через панель | MCP Router |
| mcphub-prototyping | L2 | Быстрое прототипирование MCP-интеграций через визуальную песочницу | Mcphub |
| fusio-api-management | L2 | Стандартизация REST API через open-source платформу | Fusio |
| n8n-mcp-visual-orchestration | L2 | Визуальная оркестрация MCP-серверов через n8n | n8n-nodes-mcp |
| postgres-mcp-admin | L2 | Глубокое администрирование PostgreSQL через MCP | Postgres MCP |
| dbhub-database-access | L2 | Универсальный SQL-шлюз для агентов (5 СУБД) | DBHub |
| supabase-mcp-management | L2 | Управление Supabase-проектами через MCP | Supabase MCP |
| devcontainer-management | L2 | Создание воспроизводимых сред разработки для агентов | Dev Containers CLI |
| cloudflare-infra-management | L2 | Управление Cloudflare Workers, R2, KV через MCP | Cloudflare MCP |
| designlang-visual-extraction | L2 | Извлечение дизайн-систем с веб-сайтов для генерации UI | Design Extract |
| harbor-harness-optimization | L2 | Автоматическая оптимизация harness'а агентов через constrained Bayesian optimization | HARBOR |
| cocoda-tool-coevolution | L2 | Ко-эволюция библиотеки инструментов и планировщика через композиционный DAG | CoCoDA |
| workflowgen-adaptive-generation | L2 | Адаптивная генерация рабочих процессов из траекторного опыта | WorkflowGen |
| pi-play-self-evolution | L2 | Автономная эволюция агентов через self-play с привилегированной самодистилляцией | π-Play |
| skill-r1-evolution | L2 | RL-эволюция навыков через верифицируемые награды | Skill‑R1 |
| skill-neologisms-modular | L2 | Модульное накопление навыков без катастрофического забывания | Skill Neologisms |
| think-with-rubrics | L2 | Внутреннее направление рассуждения по критериям (рубрикам) | Think‑with‑Rubrics |

## Категория 6: Трейдинг и Охота (ARIA Trading)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| spoof-wall-buster | L2 | Детекция ложных стен и автоматическая контратака на спуфера. | ARIA Core |
| latency-arbitrage-detector | L2 | Обнаружение HFT-ботов по аномально быстрым реакциям на пробои. | ARIA Core |
| dma-flow-mimic | L2 | Маскировка под DMA-поток (рыночные ордера, имитация). | ARIA Core |
| mimic-cscalp-trader | L2 | Эмуляция розничного трейдера в CScalp (задержки, ручное дробление, отмены). | ARIA Core |
| arb-unlock-hunter | L2 | Охота на шорт перед разблокировками токенов (low float / high FDV). | ARIA Core |
| mc-fdv-anomaly-detector | L2 | Сканер проектов с аномальным соотношением MC/FDV. | ARIA Core |
| tradememory-owm | L2 | Outcome-Weighted Memory (5 когнитивных слоёв). | TradeMemory Protocol |
| preflight-risk-gate | L1 | 5-факторная pre-trade проверка. | TradeMemory Protocol |
| mev-scanner | L2 | Детекция Sandwich, JIT, FlashArb атак. | ARIA Core |
| market-maker-hunter | L2 | Детекция Spoofing, StopHunting, WashTrading. | ARIA Core |
| quantdinger-research | L2 | AI-квантовое исследование рынка с генерацией стратегий. | QuantDinger |
| defi-quant | L2 | AMM-математика, MEV-аукционы, Flashbots. | ARIA Core |
| tradingview-mcp-analysis | L2 | Технический анализ (30+ индикаторов), бэктестинг (6 стратегий), скрининг | TradingView MCP |
| quantdinger-platform-mastery | L2 | Полный цикл AI-квантового трейдинга (исследование → бэктест → исполнение) | QuantDinger |
| ccxt-mcp-crypto-gateway | L2 | Универсальный доступ к 100+ криптобиржам через единый MCP-интерфейс | CCXT MCP Server |
| alphavantage-mcp-fundamental-data | L2 | Фундаментальный анализ, макроэкономика, сентимент, инсайдерские транзакции через Alpha Vantage MCP | Alpha Vantage MCP Server (официальный) |
| arkham-intel-platform | L2 | Ончейн-разведка: кластеризация кошельков, трассировка средств, AI-инсайты | Arkham Intel |
| montewalk-stochastic-modeling | L2 | Симуляции Монте-Карло, VaR/CVaR, оптимизация портфеля | MonteWalk |
| quest-deep-research-agent | L2 | Автономный deep research агент для рыночной разведки | Quest |
| fincad-debiasing | L2 | Debiasing торговых стратегий от parametric look-ahead bias | FinCAD |
| ecm-forecast-correction | L2 | Пост-процессинговая коррекция ошибок прогнозов | ECM |
| rl-cvar-dynamic-risk | L2 | Динамический риск-менеджмент через RL с CVaR барьерами | RL-CVaR |
| nexgendata-finance-mcp | L2 | Оперативный скрининг рынков, новости, сырьевые товары | NexGenData Finance MCP |
| financial-datasets-fundamental-analysis | L2 | Фундаментальные данные: отчёты, мультипликаторы, ESG, инсайдеры | Financial Datasets MCP |
| quantdinger-vue-dashboard | L2 | Визуальный HITL-мониторинг стратегий QuantDinger | QuantDinger-Vue |
| quantdinger-mobile-monitoring | L2 | Мобильный мониторинг стратегий QuantDinger | QuantDinger-Mobile |
| gnn-graph-encoder | L2 | Графовый энкодер для прогностических моделей с оценкой статистической значимости | GNN for Financial TS |
| tip-pfn-early-warning | L2 | Система раннего предупреждения о критических переходах (tipping points) | TipPFN |
| ijkonet-dynamics-recovery | L2 | Восстановление скрытой динамики рынка по фрагментарным данным | iJKOnet |
| rarecp-uncertainty-calibration | L2 | Regime-aware калибровка неопределённости прогнозов через Conformal Prediction | RareCP |
| graphic-graph-icl | L2 | Графовое In-Context Learning для табличных и реляционных данных | GraphIC |
| kumorfm2-graph-foundation | L2 | Foundation model для реляционных/графовых данных (In-Context + Fine-Tuning) | KumoRFM-2 |
| tradingbench-evaluation | L2 | Специализированный бенчмарк для оценки LLM-трейдинговых агентов | TradingBench |

## Категория 7: Кодинг и разработка (Coding & Development)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| agent-factory | L2 | Создание агентов по требованию (Markdown Agent Blueprint). | ARIA Core |
| swarm-coding | L2 | Роевое кодирование с планами Plan-as-Code и изолированными средами. | Kimi K2.6, Claude Code Swarm |
| serena-semantic-edit | L2 | Семантическое редактирование кода (40+ языков). | Serena |
| code2prompt | L2 | Интеллектуальная подготовка контекста кодовой базы для LLM. | Code2Prompt |
| fastmcp-create | L2 | Высокоуровневое создание MCP-серверов на Python. | FastMCP |
| fastapi-mcp-zero-config | L2 | Zero-config адаптер FastAPI → MCP. | FastAPI-MCP |
| mcpo-bridge | L2 | Универсальный MCP-to-OpenAPI прокси. | mcpo |
| eino-go-agents | L2 | Нативные Go AI-агенты (Eino). | Eino |
| mcp-go-sdk | L2 | Стандартный Go MCP SDK. | mcp-go |
| klavis-strata | L2 | Универсальный MCP-маршрутизатор с OAuth. | Klavis AI |
| lemonade-sdk | L2 | Легковесный AI-SDK для агентов. | Lemonade |
| langroid-actor | L2 | Actor-модель мультиагентной оркестрации. | Langroid |
| fastagent-highlevel | L2 | Высокоуровневая операционная система для агентов. | fast-agent |
| copilotkit-ui | L2 | Интерактивные AI-интерфейсы и ко-агенты в React. | CopilotKit |
| mcp-agent | L2 | ReAct‑агент с AugmentedLLM и инструментами MCP. | mcp-agent |
| praisonai-microagents | L2 | Микросекундные агенты (Python) с параллельными задачами. | PraisonAI |
| swarm-orchestration | L2 | Enterprise‑оркестрация роев с heartbeat, TTL и failure recovery. | Swarms, Cyrus Agents, Agent Swarm Resilience |
| moss-self-evolution | L2 | Автономная эволюция кода через source-level rewriting | MOSS |
| deltabox-sandbox-rollback | L2 | Мгновенные чекпоинты и откат состояния песочницы | DeltaBox |
| shadcn-ui-mcp-integration | L2 | Генерация UI-компонентов по стандарту shadcn/ui | shadcn-ui-mcp-server |
| celo-composer-kit | L2 | Создание dApps на Celo через MCP-инструменты | Composer Kit MCP |
| gemini-sdk-mastery | L2 | Программный доступ к Gemini через официальный Python SDK | Google GenAI SDK |
| mcp-java-sdk-mastery | L2 | Создание enterprise MCP-серверов на Java | MCP Java SDK |
| coplaydev-unity-mcp-mastery | L2 | 3D-визуализация и симуляции через Unity MCP | CoplayDev Unity MCP |
| notte-web-agent-framework | L2 | Создание веб-агентов с гибридными рабочими процессами и MCP | Notte |
| rao-recursive-delegation | L2 | Рекурсивная декомпозиция задач через RL-обучение делегированию | RAO |
| graft-tool-planning | L2 | Графовое планирование цепочек инструментов с учётом зависимостей | GRAFT |
| memcoder-private-library | L2 | Многомерная эволюционирующая память для кодогенерации с приватными библиотеками | MEMCoder |
| vcrd-calibrated-distillation | L2 | Калиброванная дистилляция рассуждений через отношение локальных валидностей | VCRD |
| caopd-calibration | L2 | Калибровка уверенности в On-Policy Distillation через разделение capability и calibration | CaOPD |
| paint-adaptive-distillation | L2 | Адаптивная интерполяция между учителем и учеником на основе частичных решений | PAINT |
| best-of-n-opd | L2 | Улучшение учительского сигнала через Best-of-N выбор траекторий | Best-of-N OPD |
| opsd-gui-grounding | L2 | On-Policy Self-Distillation для GUI-grounding задач | OPSD for GUI Grounding |
| longact-intrinsic-rl | L2 | Использование внутренних паттернов активации модели как дополнительного RL-сигнала | LongAct |
| terminus-lightweight-executor | L2 | Использование легковесных моделей (4B) для узких агентных задач | Terminus-4B |

## Категория 8: Мультимодальные и HITL навыки (Multimodal & HITL)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| chart-visualization | L2 | Автоматический выбор типа диаграммы (AntV, 26+ типов). | AntV MCP |
| drawio-diagram | L2 | Генерация диаграмм на естественном языке. | next-ai-draw-io |
| excalidraw-canvas | L2 | Интерактивная визуальная доска. | Excalidraw MCP |
| pptagent-presentation | L2 | Агентная среда генерации презентаций с визуальной саморефлексией. | PPTAgent |
| figma-full-control | L2 | Полный контроль дизайна Figma через MCP (40+ инструментов). | Cursor Talk To Figma MCP |
| penpot-open-design | L2 | Открытая дизайн-платформа с design tokens. | Penpot |
| magic-ui | L2 | Мгновенная генерация React-компонентов (shadcn/ui). | Magic MCP |
| excel-finance | L2 | Работа с финансовыми таблицами без Microsoft Excel. | Excel MCP |
| codeinterpreter | L2 | Песочница для анализа данных (Python). | Code Interpreter API |
| cad-3d-modeling | L2 | Параметрическое 3D-моделирование и симуляция (FreeCAD + Godot). | FreeCAD MCP, Godot MCP |
| blender-3d | L2 | Профессиональное 3D-моделирование, анимация и рендеринг. | BlenderMCP |
| pollinations-media | L2 | Легковесная генерация AI-медиа (изображения, аудио, 3D, видео). | Pollinations |
| realchar-avatar | L2 | Real-time голосовой и видео HITL с аватаром. | RealChar |
| whatsapp-channel | L2 | Коммуникационный мост к WhatsApp. | WhatsApp MCP |
| fonoster-telecom | L2 | Программируемые телекоммуникации и голосовой HITL. | Fonoster |
| openclaw-personal | L2 | Персональный AI-ассистент (361k+ звёзд, 22+ каналов). | OpenClaw |
| hermes-self-evolving | L2 | Self-Evolving Agent с learning loop. | Hermes Agent |
| openwebui-interface | L2 | Self-hosted AI интерфейс с ChatGPT-подобным UI. | Open WebUI |
| dify-platform | L2 | Визуальная операционная система AI (141k звёзд). | Dify |
| langflow-visual | L2 | Визуальный AI-конструктор (14.7k звёзд). | LangFlow |
| n8n-automation | L2 | Универсальная платформа автоматизации (70.6k звёзд, 400+ интеграций). | n8n |
| osaurus-community | L2 | Community-driven MCP-совместимая AI-платформа. | Osaurus |
| interactive-feedback-loop | L2 | Интерактивный цикл обратной связи ИИ‑человек с Web UI и десктоп‑приложением. | mcp-feedback-enhanced |
| playwright-automation | L2 | Кросс‑браузерная автоматизация и тестирование через Playwright. | Playwright MCP |
| steel-browser-sandbox | L2 | Изолированная браузерная песочница для безопасного веб‑скрапинга. | Steel Browser |
| desktop-commander | L2 | Управление терминалом, файловой системой и приложениями через MCP. | DesktopCommanderMCP |
| vexa-voice-hitl | L2 | Серверный голосовой HITL через Telegram, веб и телефонные звонки | Vexa AI |
| py-xiaozhi-voice-hid | L2 | Edge/IoT-голосовое взаимодействие с wake-word активацией | py-xiaozhi |
| promptx-role-engineering | L2 | Создание экспертных HITL-интерфейсов через ролевые промпты | PromptX |
| peekaboo-screen-context | L2 | Захват контента активного окна для ситуационной осведомлённости | Peekaboo |
| apple-macos-automation | L2 | Взаимодействие с нативными приложениями macOS (Сообщения, Почта, Заметки) | Apple MCP |
| smart-home-context | L2 | Взаимодействие с умным окружением (Home Assistant) | HA-MCP |
| hermes-agent-mastery | L2 | Работа с самообучающимся персональным AI-ассистентом | Hermes Agent |
| google-workspace-orchestration | L2 | Оркестрация Google Workspace (Gmail, Drive, Calendar, Docs, Sheets) | Google Workspace MCP |
| mcp-agent-mail-client | L2 | Чтение и отправка почты через IMAP/SMTP | MCP Agent Mail |
| office-word-mcp-documentation | L2 | Создание и редактирование Word-документов через MCP | Office Word MCP Server |
| trilium-knowledge-interface | L2 | Визуальный HITL-интерфейс для графа знаний | TriliumNext Notes |
| md2wechat-formatting | L2 | Конвертация Markdown в формат WeChat | md2wechat-skill |
| ios-simulator-management | L2 | Управление iOS-симулятором через MCP | iOS Simulator MCP |
| vac-visual-verification | L2 | Верификация визуальных отчётов (соответствие текста графикам) | VAC |
| ga4-conversational-analytics | L2 | Разговорная аналитика Google Analytics 4 через MCP | Google Analytics MCP |
| ui-copilot-gui-automation | L2 | Долгосрочная GUI-автоматизация с Memory Decoupling и TIPO-обучением | UI-Copilot |
| gui-r1-reasoning | L2 | Reasoning-first GUI-агент с R1-стилем рассуждения перед действием | GUI‑R1 |
| cogagent-visual-perception | L2 | Высокоточное визуальное восприятие GUI через dual-resolution inputs | CogAgent |
| mobile-agent-execution | L2 | Надёжное GUI-выполнение с ReAct-рефлексией и перепланированием | Mobile-Agent |
| echotrail-actionable-memory | L2 | Межсессионное накопление GUI-опыта через Actionable Memory Bank | EchoTrail-GUI |
| webvoyager-navigation | L2 | Специализированная веб-навигация через Playwright с MCP-интеграцией | WebVoyager |
| appagent-exploration | L2 | Автономное исследование GUI-приложений с построением документации | AppAgent |

## Категория 9: Исследовательские навыки (Research)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| deep-research | L2 | Автономное глубокое исследование с десятками параллельных поисков. | GPT Researcher |
| firecrawl-scrape | L2 | Превращение любой веб-страницы в чистый markdown. | Firecrawl MCP |
| exa-neural-search | L2 | Нейронный семантический поиск с автономными multi-agent исследователями. | Exa MCP |
| u14-multi-engine | L2 | Расширенный исследовательский MCP-сервер с 11 поисковыми движками. | U14 Deep Research |
| trafilatura-extract | L2 | Легковесное извлечение текста и метаданных без браузера. | Trafilatura |
| youtube-transcript | L2 | Извлечение транскриптов YouTube для анализа. | YouTube Transcript API |
| xiaohongshu-sensor | L2 | Доступ к данным платформы Xiaohongshu (300M+ пользователей). | Xiaohongshu MCP |
| trendradar-pulse | L2 | Глобальный пульс технологий (GitHub, Hacker News). | TrendRadar |
| misp-correlation | L2 | Автоматическая корреляция событий безопасности. | MISP |
| ultrarag-experiments | L2 | MCP-нативный исследовательский RAG с встроенными бенчмарками. | UltraRAG |
| perplexity-mcp-search | L2 | Оперативный веб-поиск с гарантированным цитированием | Perplexity MCP |
| papersgpt-research-autopilot | L2 | Автономный обзор научной литературы через AutoPilot | PapersGPT for Zotero |
| brightdata-web-intelligence | L2 | Веб-разведка через enterprise-инфраструктуру BrightData | BrightData MCP |
| fastmcp-threatintel-analysis | L2 | Multi-source Threat Intelligence с AI-анализом и отчетностью | FastMCP ThreatIntel |
| sycek-osint-platform | L2 | Коммерческая OSINT-платформа (утечки, Twitter, WHOIS) | Sycek MCP |
| osint-tools-mcp | L2 | Легковесная проверка юзернеймов, email, паролей, WHOIS | OSINT Tools MCP |
| osint-toolkit-network-recon | L2 | Легковесная сетевая разведка (Nmap, dnstwist, WHOIS) | OSINT Toolkit MCP |
| radar-geospatial-analysis | L2 | Геопространственный анализ через Radar MCP | Radar MCP |
| slackdump-data-harvesting | L2 | Сбор разведывательных данных из Slack-сообществ | slackdump |
| graph-react-investigation | L2 | Пошаговое исследование графов через ReAct-парадигму | GraphReAct |
| dracula-intermediate-feedback | L2 | Использование обратной связи на промежуточных шагах deep research | DRACULA |

## Категория 10: Наблюдаемость и мониторинг (Observability)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| greptimedb-observability | L2 | Единый фундамент для метрик, логов и трейсов с SQL‑интерфейсом. | GreptimeDB |
| phoenix-llm-traces | L2 | Трассировка и оценка LLM‑вызовов (Arize Phoenix). | Phoenix |
| kubeshark-network | L2 | Глубокая сетевая наблюдаемость с eBPF (перехват трафика, анализ пакетов). | Kubeshark |
| context-integrity-daemon | L1 | (см. Категорию 3) Фоновая проверка целостности ключевых параметров сессии. | ARIA Core |
| auto-memory-audit | L2 | (см. Категорию 3) Ежедневный аудит памяти. | ARIA Core |
| grafana-mcp-observability | L2 | Доступ к дашбордам, метрикам, логам и алертам Grafana через MCP | Grafana MCP |

---

**Прогрессивное раскрытие:**
- **L1** — метаданные (~100 токенов), всегда в контексте.
- **L2** — инструкции (<5000 токенов), загружаются при активации навыка.

**Доступ:** все навыки доступны через `skills-registry-mcp` и команду `/skill-find` в Telegram.
