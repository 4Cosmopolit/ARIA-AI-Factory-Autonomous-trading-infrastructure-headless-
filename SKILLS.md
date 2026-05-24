# SKILLS.md — Реестр навыков ARIA AI‑Factory v13.01

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

## Категория 4: Токен-экономия (Token Economy)

| Навык | Уровень | Описание | Источник |
|:---|:---|:---|:---|
| token-aware-routing | L1 | Маршрутизация запросов к дешёвым моделям для простых задач. | ARIA Core |
| tool-limit-enforcer | L1 | Жёсткий лимит числа вызовов MCP-инструментов за сессию. | ARIA Core |
| token-auditor | L2 | Ежедневный анализ структуры затрат токенов (полезная работа vs шум). | ARIA Core |
| semantic-tool-selection | L1 | Семантический отбор инструментов (сокращение контекста на 99.1%). | vLLM Semantic Router |
| bifrost-gateway | L2 | Автоматическое переключение между провайдерами с кэшированием. | Bifrost |

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

---

**Прогрессивное раскрытие:**
- **L1** — метаданные (~100 токенов), всегда в контексте.
- **L2** — инструкции (<5000 токенов), загружаются при активации навыка.

**Доступ:** все навыки доступны через `skills-registry-mcp` и команду `/skill-find` в Telegram.
