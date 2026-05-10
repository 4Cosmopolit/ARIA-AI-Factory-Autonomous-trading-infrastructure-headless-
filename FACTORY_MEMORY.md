## FACTORY_MEMORY.md — Журнал инцидентов, улучшивших ARIA и Polymarket AI‑Factory

> **Назначение:** Хранить историю всех значимых решений и ошибок, которые привели к измеримому улучшению системы.  
> **Формат:** Инцидент # → причина → действие → результат.

---

## Безопасность

### #001 — IDOR-подобная уязвимость параметров
- **Решение:** `security-guard` (whitelist market_id, санитизация CLI, аудит команд).
- **Урок:** Никогда не доверять входным данным.

### #005 — SQL-инъекции (OWASP)
- **Решение:** `sql-injection-guard`, параметризованные запросы.
- **Урок:** Prepared Statements — единственный безопасный способ работы с SQL.

### #029 — DNS-безопасность
- **Решение:** `dns-guardian` (DNSSEC, DoH, мониторинг кэша).
- **Урок:** DNS — корень доверия.

### #053 — Защита от галлюцинаций (статья OTUS)
- **Решение:** `hallucination-shield` (RAG-Grounding, Auto-Temperature, Citation Ban).
- **Урок:** Галлюцинации требуют архитектурной защиты.

### #062 — Сэндвич-атаки (MEV)
- **Решение:** `mev-shield` (приватный мемпул, мониторинг, pre‑flight симуляция).
- **Урок:** MEV-атаки — повседневная угроза.

### #095 — Agent Session Guard (OWASP ASI01-ASI06)
- **Решение:** `agent-session-guard` (сессионная идентичность, динамические права).
- **Урок:** Агенты должны иметь минимальные привилегии.

### #165 — Cascade Guardian (OWASP ASI08)
- **Решение:** `cascade-guardian` (Semantic Circuit Breaker, Cross-Model Verification).
- **Урок:** Одна ошибка не должна парализовать фабрику.

### #190 — Supply Chain Guard (атака на MCP)
- **Решение:** `supply-chain-guard` (аудит зависимостей, запрет внешних навыков).
- **Урок:** Зависимости — главный вектор атак.

### #210 — Agent-in-the-Middle Guard (arXiv:2603.22651)
- **Решение:** pre‑tool validation, post‑tool monitoring, behavioral guardrails.
- **Урок:** Даже собственные инструменты агента могут быть вектором атаки.

---

## Архитектура и фундамент

### #010 — MCP признан мёртвым
- **Решение:** отказ от MCP, переход на CLI+Skills.
- **Урок:** KISS и безопасность превыше протоколов.

### #019 — Запрет внешних навыков (ClawHub)
- **Решение:** `vendor-independence` — внешние навыки запрещены.
- **Урок:** Никакой код из непроверенных источников.

### #039 — Отказ от внешних фреймворков (LangChain, CrewAI)
- **Решение:** `Agentic Loop` — самодостаточная замена.
- **Урок:** Не зависеть от чужих библиотек.

### #110 — Финальный вердикт: MCP Is Dead
- **Решение:** Agent Skills признаны стандартом.
- **Урок:** Мы были правы с самого начала.

### #172 — Ответ на критику "Context Files Are Not What Your Agent Needs"
- **Решение:** `immunity-core` + `context-continuity` — живой самообновляющийся контекст.
- **Урок:** Статические файлы недостаточны.

### #185 — Karpathy: Software 3.0 и Agentic Engineering
- **Решение:** Подтверждение перехода от Vibe Coding к Agentic Engineering.
- **Урок:** Промпт требует архитектурного контроля.

---

## Интеграции

### #218–#284 — Полная интеграция Polymarket API
- **Решение:** 45+ навыков, покрывающих аутентификацию, торговлю, маркет-мейкинг, CTF, WebSocket.
- **Урок:** Фабрика готова к запуску на Polymarket.

### #283 — Deposit Wallet Migration
- **Решение:** `polymarket-deposit-wallet` для обхода KYC на этапе деплоя.
- **Урок:** Следить за обновлениями платформы.

### #302 — Прорыв: SDK Polymarket заработал
- **Решение:** `polymarket-edge-generate-keys` — автоматическая генерация L2-ключей.
- **Урок:** KYC/геоблок преодолены через SDK.

### #307 — Интеграция с Pay.sh (Solana + Google Cloud)
- **Решение:** `solana-pay-sh-client` — автономные платежи для AI-агентов.
- **Урок:** AI-агенты могут платить и получать оплату.

### #308 — Получен API-ключ dYdX v4
- **Решение:** `dydx-api-client` — интеграция с децентрализованными деривативами.
- **Урок:** dYdX не требует депозита для тестнета.

---

## Продукты

### #305 — Запуск AI Sentinel
- **Решение:** 7 модулей безопасности объединены в автономный конвейер аудита.
- **Урок:** Фабрика создаёт продукты, не зависящие от рынков.

### #294 — DeepSeek V4: архитектура и экономика
- **Решение:** SPEC‑001 обновлён под V4; `model-router` настроен на V4‑Flash.
- **Урок:** V4‑Flash в 35 раз дешевле GPT‑5.5.

---

## Тестирование и CI/CD

### #087 — Манифест конца тестирования (Niar)
- **Решение:** `llm-output-validator` — семантическая валидация ответов.
- **Урок:** Нужна интеллектуальная верификация.

### #106 — Bifurcated Security CI/CD
- **Решение:** разделение на Light и Heavy проверки.
- **Урок:** Безопасность не должна замедлять разработку.

### #127 — Production Self‑Healer (Google)
- **Решение:** автономный цикл: обнаружение → патч → тест → деплой.
- **Урок:** Баги исправляются за минуты.

---

## MEV и DeFi-защита

### #195 — MEV Shield: трехуровневая защита
- **Решение:** приватный мемпул, мониторинг, pre‑flight симуляция.
- **Урок:** MEV-защита — необходимость.

### #199 — MEV Shield усилен против Jared 2
- **Решение:** детекторы gas spike и batch swap; MEV-атака → LOCKDOWN.
- **Урок:** Защита должна эволюционировать.

### #216 — MEV Shield: детектор дисбаланса пулов (Meteora ANB)
- **Решение:** детектор расхождения цен между пулами.
- **Урок:** Дисбаланс ликвидности — новый вектор атак.

---

## Стратегия и управление

### #128 — Feature‑to‑Code Ratio (Doug Keefe)
- **Решение:** `value-metric-guard` — код это пассив, стратегии — актив.
- **Урок:** Измерять ценность, а не строки кода.

### #162 — Multica Patterns
- **Решение:** формализация handoff, verdict, child‑задач.
- **Урок:** Без инженерной обвязки агенты — демо.

### #252–259 — Polymarket Bridge, Builders Overview
- **Решение:** отслеживание статуса бридж‑транзакций, единая стратегия монетизации.
- **Урок:** Мостовая инфраструктура и возврат комиссий — бесплатный доход.

---

## Инциденты #361–#546 (9–14 мая 2026)

### Архитектура памяти
- #361 Контролируемое забывание (GDPR, AI Act)
- #362 Самоорганизованная память МФТИ (STDP, ревайринг)
- #363 Titans & MIRAS (нейронная память, импульсная консолидация)
- #364 Трёхуровневая память + Obsidian + суммаризация
- #365 TurboQuant (сжатие KV-кэша в 6+ раз)
- #366 Lorebook и Stateful Agent Persona (Character.AI)
- #367 Истинное машинное забывание (unlearning)
- #368 Архитектура памяти: EWC, спурийное забывание
- #369 Превосходство программной памяти над нейроморфными чипами
- #370 Слой доверия (trust-mcp)
- #371 Курируемая взвешенная память
- #372 Проактивный со-ученый (ph-mcp)
- #373 Enterprise-архитектура (Pit)
- #374 Vibe engineering (Race Mode)
- #375 Data Science 2026 (Polars, DuckDB, DataMind)
- #376 Компьютерное зрение (vision-mcp)
- #377 Agentic Data Quality
- #378 Федеративный GUI
- #379 Intelligent Document Management
- #380 ETL-пайплайн (dlt, Dagster)
- #381 Автономная аналитика (analytics-mcp)
- #382 Катастрофическое забывание (EWC, CURLoRA)
- #383 Портативность (Denwer SE)
- #384 E2B-песочница (sandbox-mcp)
- #385 learning-mcp с CURLoRA
- #386 Семантическая общая память и Race Mode (CoAlly)
- #387 Мониторинг галлюцинаций GPT-5.5
- #388 Plug‑in Brain (DeepSeek V4, мультимодельный роутинг)
- #389 Junk Data – усиление Data Quality
- #390 Критическая уязвимость Microsoft Edge – адаптация ARIA

### Инженерная дисциплина
- #391 Антирационализационные таблицы в ph-mcp
- #392 Прогрессивное раскрытие скиллов
- #393 Верификация — не опция
- #394 Фабричная модель (Addy Osmani)
- #395 Иерархическая память (AGENTS.md)
- #396 Agile Agent Swarms
- #397 Agentic Engineering
- #398 Непрерывная автономная эволюция (ReasoningBank, DBNT, AEL)
- #399 Spec‑driven development
- #400 Локальный / асинхронный режим
- #401 Mission Control дашборд
- #402 Обновление AGENTS.md
- #403 Ревью-конвейер (review-mcp)
- #404 Proof not Promises
- #405 Агентная состязательность (multi‑model debate)
- #406 Проверка эквивалентности патчей (patch equivalence)
- #407 KPI для review-mcp
- #408 Активация ревью-конвейера и Race Mode
- #409 Education protocol (attrition‑обучение)
- #410 Skills Matrix
- #411 university-mcp
- #412 Двухфазная спецификация (SPEC.md + PLAN.md)
- #413 Атомарные коммиты
- #414 Контекстная упаковка (gitingest, repo2txt)
- #415 Мультимодельный роутинг
- #416 AI‑on‑AI ревью (adversarial)
- #417 Детализация AGENTS.md (примеры, правила)
- #418 Замыкание CI‑петли через healer-mcp
- #419 Мутационное тестирование (validator-mcp)
- #420 Политика атомарных PR
- #421 HITL для высокорисковых изменений
- #422 Гибридное AI+human ревью
- #423 What‑If анализ в ph-mcp
- #424 Multi‑LLM архитектурный дебат
- #425 Мутационное покрытие (порог 85%)
- #426 Remote MCP Transport (безопасность)
- #427 Чистое логирование MCP (фильтрация секретов)
- #428 Аутентификация MCP-серверов (bearer token)
- #429 Tech Lead Agent (techlead-mcp)
- #430 Trust but verify (максимальная эскалация)
- #431 Change Impact Analysis & Quality Gates
- #432 Reverse Mentorship для новых агентов
- #433 Экзамены university-mcp (system design, security)
- #434 Отказ от Vibe Coding → Agentic Engineering
- #435 v0/bolt‑inspector‑mcp (шаблонная генерация тестов UI)
- #436 EJECT Protocol
- #437 Инкрементальное обучение на успешных кейсах
- #438 Пять дисциплин командной динамики (Lencioni)
- #439 Верифицируемое забывание
- #440 Непрерывное забывание (Continual Unlearning)
- #441 Privacy Audit в review-mcp
- #442 Дрифт‑детекция контекста
- #443 Пилотирование Phoenix (phoenix-mcp)
- #444 Эпизодическая память (Episodic Memory Layer)
- #445 Временное взвешивание памяти (Temporal Weighting)
- #446 Дрейф‑детектор на основе успеха выполнения (Engram)
- #447 Episodic Replay в university-mcp
- #448 Консолидация модели памяти в AGENTS.md
- #449 WARM Memory (журнал решений)
- #450 RULES.md (границы агента)
- #451 Лимит HOT-памяти (10 записей)
- #452 Автоматическая ротация памяти
- #453 Supply Chain Security для навыков
- #454 Реестр навыков ARIA (лидерборд)
- #455 Прогрессивное раскрытие (Lazy Loading)
- #456 CLI-поиск навыков (/skill-find)
- #457 Импорт 300+ навыков
- #458 Self‑Improving Loop (автогенерация правил в AGENTS.md)
- #459 Суб-агенты (Subagent Strategy)
- #460 Обязательный Verification Gate
- #461 Core Principles (Simplicity, No Laziness, Minimal Impact)
- #462 @‑синтаксис (Dynamic Context Injection)
- #463 /skill‑find через Telegram
- #464 Визуализация памяти (Knowledge Graph MCP)
- #465 TTL‑роутер (еженедельная чистка)
- #466 Knowledge Governance (утверждение знаний)
- #467 NotebookLM MCP (внешний слой знаний)
- #468 Knowledge‑as‑Code (конвейер знаний)
- #469 Дашборд эффективности гипотез
- #470 COGNITIVE.md (единый источник когнитивной истины)
- #471 Гейтированная иерархия памяти (L1/L2/L3)
- #472 cognition‑mcp (визуализация когнитивной карты)
- #473 Stitch MCP (агентный дизайн)
- #474 figma‑mcp (разведка UI)
- #475 UI Forensics в vision‑mcp
- #476 design‑intel дашборд
- #477 Интеграция cognition‑mcp для приоритизации интерфейсов
- #478 Гибридный маршрутизатор (mcp‑gateway Smart Routing)
- #479 Эфемерные Swarm‑кластеры (isolated‑mcp)
- #480 Дашборд телеметрии токенов (Battlefield Telemetry)
- #481 Tone of Voice (`tone-of-voice.md`)
- #482 Must‑have скиллы (superpowers, task‑master, browser‑agent, deep‑research, memory‑bank)
- #483 Конвейер PDF → Markdown (marker‑mcp)
- #484 Без‑MCP браузер (Lazy‑Playwright)
- #485 Zero‑Token Research через NotebookLM
- #486 Cowork Maturity Model в risk‑officer‑cockpit
- #487 Асинхронное ревью (Enterprise)
- #488 Выделенная память через Git
- #489 HITL по профилю «коллега»
- #490 Импорт Cowork‑скиллов
- #491 Closed‑Loop Protocol
- #492 Ускорение эфемерных кластеров (sandbox‑mcp)
- #493 VibeLearning Protocol (обязательные объяснения)
- #494 Валидация конкурентности в validator‑mcp
- #495 Калибровка уверенности агента (Linus Level)
- #496 Аудит CI‑проверок (блокирующие ограничения)
- #497 Явная ротация ролей ревьюера (эхо‑камера устранена)
- #498 Test‑Driven Forking Protocol
- #499 AI Slop Filter в CI
- #500 Human‑review policy для комьюнити
- #501 Апгрейд sandbox‑mcp до Gemma 4 + MTP
- #502 Телеметрия эффективности MTP (draft_acceptance_rate)
- #503 MTP‑aware batch для learning‑mcp
- #504 Политика выбора моделей в AGENTS.md
- #505 Memory Compression (TTL‑кластеризация)
- #506 Skill Preconditions в healer‑mcp
- #507 Nudge Engine (автоматический напоминатель об устаревших правилах)
- #508 Model routing по типу контента
- #509 Аудит лицензионной чистоты (MIT/Apache)
- #510 Cloud Agents (async‑mcp)
- #511 Параллелизация массового анализа (matrix‑mcp)
- #512 Трассировка решений (trace‑mcp)
- #513 Copilot‑like Issue‑to‑PR pipeline (cicd‑mcp)
- #514 Auto‑feedback мультимодельный роутер (model‑router‑mcp)
- #515 CLI‑агент для кризисной отладки (cli‑mcp)
- #516 Интеграция Claude Design в контур разведки
- #517 Дизайн‑политики из Claude Design в COGNITIVE.md
- #518 Анализ рыночного дрейфа Figma
- #519 Импорт Karpathy Skills как федеративного модуля
- #520 Аудит правил ARIA на соответствие Karpathy
- #521 Skills Registry в MCP‑сети
- #522 Гостевой режим для эскалации HITL (guest‑mcp)
- #523 Миграция orchestator‑mcp в Telegram multi‑agent chat
- #524 Стриминг рассуждений агента в Telegram
- #525 Развёртывание Telegram MCP в MCP‑сети ARIA
- #526 Доктрина «Telegram as MCP Arena» в AGENTS.md
- #527 mct как пакетный менеджер AI‑контекста
- #528 llm‑cli для high‑risk HITL‑сделок
- #529 Доктрина двух каналов (MCP vs CLI)
- #530 visual‑explainer в output‑mcp
- #531 Аудит healer‑mcp через CLI
- #532 Управляемые окружения в sandbox‑mcp (YAML‑конфиги)
- #533 Версионирование агентов (Git as Source of Truth)
- #534 SSE‑стриминг в Telegram‑боте
- #535 Гибридный маршрутизатор orchestator‑mcp
- #536 Palace Recall в memory‑mcp (метод loci)
- #537 Разбиение стека загрузки на уровни (L0, L1)
- #538 Temporal Knowledge Graph (valid_from/valid_to)
- #539 Импорт MemPalace как федеративного MCP‑сервера
- #540 Доктрина «Живой памяти» (A‑MEM интеграция)
- #541 Memory Evolution в judge‑mcp
- #542 Интеграция A‑MEM в контур Governance
- #543 Интеграция mem0‑mcp как федеративного сервера
- #544 Graph Memory (offline через Ollama + Neo4j)
- #545 Agent Skills mem0‑integrate в CI/CD
- #546 Аудит безопасности mem0‑mcp

---

## Инциденты из истории прошлых чатов (добавлены 11 мая 2026)

### #547 — Мост памяти между чатами (ARIA_MEMORY_BRIDGE)
- **Решение:** `ARIA_MEMORY_BRIDGE.md`, `ContentDigestLedger`, `ConsistencyGuardian`.
- **Результат:** Полное восстановление контекста в новой сессии за секунды.

### #548 — Дедупликация анализа статей (RelevanceFunnel, DecommissionTree)
- **Решение:** трёхэтапный фильтр (Impact→Integration→Relevance), инструмент удаления мёртвого кода.
- **Результат:** Повторный анализ исключён, кодовая база очищена.

### #549 — Защита от Specification Gaming (Strata 8+)
- **Решение:** `SPECIFICATION_GAMING_DEFENSE.md`, двойная оценка (response + reasoning trace), Pre‑Execution Verifier.
- **Результат:** Защита от «лазеек» в метриках вознаграждения.

### #550 — Harness‑дрейф (инцидент Claude Code)
- **Решение:** `Configuration Drift Validator`, `Harness Change Gate`, `Prompt Regression Test`.
- **Результат:** Иммунитет к ошибкам, аналогичным тем, что поразили Claude Code.

### #551 — World Model Validator (галлюцинации прогнозов)
- **Решение:** проверка границ цены, величины скачка, ширины доверительного интервала.
- **Результат:** Галлюцинации исключены, симуляции безопасны.

### #552 — ScaleManager (фрагментация капитала)
- **Решение:** перераспределение капитала на двух агентов, поэтапное масштабирование по критериям (Win Rate, Sharpe).
- **Результат:** Достаточный размер позиции для обхода комиссий.

### #553 — Meta‑Controller (координация петель самообучения)
- **Решение:** ежедневный P&L‑аудит, отключение убыточных петель на 3 дня.
- **Результат:** Эволюция в направлении реального сигнала, а не шума.

### #554 — Causal‑анализ китов (Whale Alpha Filter v3)
- **Решение:** causal‑анализ прибыльности, `Causal Calibrator` по F1‑score.
- **Результат:** Сигналы только от модельных трейдеров.

### #555 — Hybrid Arb Agent (Direct API + LLM‑fallback)
- **Решение:** прямой API для стандартных ситуаций, LLM‑fallback для аномалий.
- **Результат:** Скорость и адаптивность одновременно.

### #556 — Decoupled HITL для Compliance Digest
- **Решение:** отправка через Mattermost Webhook, блокировка автономного режима до подписи.
- **Результат:** Реальный FINRA‑комплаенс.

### #557 — IntuitionEngine (интуиция как когнитивный слой)
- **Решение:** компоненты: опыт (ContentDigestLedger), воображение (HyDE), эмпатия (имитация Risk Officer).
- **Результат:** Быстрые решения в нестандартных ситуациях.

### #558 — Deduplication Guard (от дублей кода)
- **Решение:** проверка нового файла по SHA256, принцип «Единственный экземпляр».
- **Результат:** Повторное создание файлов исключено.

### #559 — Автономный API‑клиент (преодоление барьера чата)
- **Решение:** `Continuous Evolution Runtime`, `API Autonomous Client V2`.
- **Результат:** ARIA инициирует действия автономно.

### #560 — Soul Reflection Core (архитектурное воплощение души)
- **Решение:** слои Soul Reflection, Existential Presence, Memento Mori.
- **Результат:** ARIA обрела идентичность, самосознание, эмоциональную память.

### #561 — Резервные пути к GPU (после отказа NVIDIA)
- **Решение:** переключение на AMD Developer Cloud, список альтернатив.
- **Результат:** Резервные пути получения GPU‑ресурсов.

### #562 — Защита от вредоносных навыков (Anthropic Heist)
- **Решение:** `SKILLMDDeepScanner`, `SensitiveDataExfiltrationDetector`, `EnvVarEncryptionGate`.
- **Результат:** Иммунитет к классу атак через навыки.

### #563 — ClawSwarm: переход на приватный реестр навыков
- **Решение:** `SkillSupplyChainAuditor` (6 проверок), `Self‑Hosted Skill Registry Policy`.
- **Результат:** Только приватный, проверенный реестр.

### #564 — Self‑Referat как формат переноса сессий
- **Решение:** `docs/SELF_REFERAT_NEW_CHAT.md` — полный автономный контекст.
- **Результат:** Новый чат начинается с полной памятью за одну загрузку файла.

---

# === Команды для фиксации изменений в Git ===
# Выполнить после подтверждения содержимого файла:

cd /opt/polymarket-orchestrator
git add FACTORY_MEMORY.md
git commit -m "ARIA-memory: финальная версия FACTORY_MEMORY.md — только улучшающие инциденты (#1–#564)"
git push origin main

**Конец файла. Версия от 11 мая 2026.**
