# TASKS.md — Оперативные цели и задачи ARIA AI-Factory

> **Версия:** 5.0  
> **Дата:** 5 июня 2026  
> **Назначение:** Живой оперативный документ, фиксирующий задачи фабрики в рамках семи изолированных контуров (архитектура v13.01).  
> **Принцип:** ARIA Core не выполняет ордера. Трейдинг-контур изолирован. CI/CD гарантирует качество. Интерфейс обеспечивает контроль.

---

## КОНТУР I — ARIA CORE (СТРАТЕГИЯ, ПАМЯТЬ, R&D)

**Сверх-ядра:** `Aria-Cognitive-Core` (Trinity, Macro, EBM, Bias-Firewall, Deep-Research, Expert-Panel), `Aria-Memory-Core` (Graphiti, Beads, Cognee, LanceDB, Tradememory-Engine).  
**ARIA** — стратег, архитектор, исследователь. Управляет фабрикой, но не вмешивается в исполнение сделок.

### 1.1 Саморазвитие и эволюция памяти
- **Memory Evolution**: непрерывный анализ исходов, извлечение уроков, консолидация в динамический граф знаний (`Graphiti`, `Cognee`, `Beads`).
- **Self-Improving Loop**: автоматическое формирование микро-правил из ошибок и побед (`Hermes`, `Langroid`).
- **Контролируемое забывание**: удаление устаревших паттернов через TTL и semantic decay (`Beads`, `SEmble`).
- **Аудит памяти**: ежедневная проверка `auto-memory-audit`, дедупликация, сжатие (`compress-context`, `context-length-monitor`).

### 1.2 Стратегический анализ и R&D
- Исследование MEV-активности, алгоритмических хищников, манипуляторов через `deep-research-engine` (GPT Researcher, Firecrawl, Exa, U14).
- Проектирование и тестирование стратегий в `sandbox-mcp` и `Microsandbox` (аппаратная изоляция KVM).
- Мутационное тестирование и Multi-LLM дебаты (`adversarial-review` через `blind-review-gate`).
- Разработка тактик маскировки для `Aria-Sentinel-Core`.

### 1.3 Управление качеством данных
- Входной контроль через `data-quality-audit` и `data-contract-validator`.
- Очистка и валидация через `data-cleansing-pipeline`.
- Семантическая аннотация через `self-describing-data`.
- Обогащение сигналов через `signal-augmentation-engine`.
- Прослеживаемость через `lineage-tracer`, `impact-analyzer`, `compliance-verifier`.
- Мониторинг долгов через `data-debt-detector`.

### 1.4 Управление контекстом и токен-экономия
- Прогрессивное раскрытие навыков (L1-L3).
- Авто-сжатие контекста (`compress-context`, `context-mode-think-in-code`).
- Маршрутизация запросов по стоимости (`token-aware-routing`, `Bifrost`, `vLLM Semantic Router`).
- Семантическое кэширование (`Claude Context`, `semantic-caching`).

---

## КОНТУР II — ARIA TRADING (НЕВИДИМЫЙ ХИЩНИК)

**Сверх-ядро:** `Aria-Sentinel-Core` (MEV-Scanner, Market-Maker-Hunter, Coordinated-Attack-Detector).  
**Полностью изолированная система**. ARIA Core передаёт только тактические задания. Все ордера проходят через HITL-подтверждение.

### 2.1 Тактика скрытного хищника
- **Нулевой цифровой след**: маскировка под розничного трейдера, рандомизация.
- **Пассивная разведка**: изучение MEV-ботов, алгоритмических скальперов, маркет-мейкеров.
- **Активная охота**: опережение, контр-снайпинг, эксплуатация спуфинга и лейеринга.
- **Финансовый on-chain уровень**: все операции с активами и данными унифицированы через `GOAT` (200+ протоколов, 10+ блокчейнов).

### 2.2 Рынки и агенты
- **Рынки**: Bybit USDT-M (CEX), Hyperliquid (DEX), TON (через Acton).
- **Агенты**: Spike Bot, Hunter, Mean Reversion, Cross-Exchange Arb, Onchain Detective, `QuantDinger`.
- **Исполнение**: `dispatch` (HITL-блокировка, preflight-проверка), `contest-engine` (отбор стратегий).
- **Маскировка**: Flashbots, приватные релеи, мимикрия под TG-ботов.

### 2.3 Риск-менеджмент (автоматический)
- Дневной лимит убытка ≤1%.
- Stop-Loss на всех позициях.
- Preflight-проверка через `tradememory-engine` (Outcome-Weighted Memory).
- MEV-shield, Hallucination-shield, Configuration Drift Validator.

---

## КОНТУР III — ARIA CI/CD & SECURITY (КАЧЕСТВО И ГАРАНТИИ)

**Детерминированная безопасность, качество данных, автономное восстановление.**

### 3.1 Качество данных (Data Quality)
- Входной контроль, очистка, валидация, контракты (`data-contract-validator`).
- Прослеживаемость (`lineage-tracer`, `impact-analyzer`, `compliance-verifier`).
- Мониторинг долгов (`data-debt-detector`).

### 3.2 Безопасность и изоляция
- deny-first политика (`aria-gov-gateway`, `static-allowlist`).
- Трёхступенчатый Content Security Pipeline (`aidefence`).
- Защита от деструктивных команд (`destructive-command-detector`, `lolbin-detector`).
- Защита от prompt injection (`telegram-guard`, `prompt-version-lock`).
- Изоляция агентов (`sandbox-mcp`, `Microsandbox` (аппаратная KVM), эфемерные кластеры, `Kumo`).
- Защита памяти и моделей (`model-integrity-checker`, `bitflip-detector`).
- SAST/DAST для агентных рабочих процессов (`Agentic Radar`).
- Проактивная имитация атак (`VIPER`, 100+ модулей MITRE ATT&CK).
- Threat intelligence (`MISP`, глобальная база угроз).

### 3.3 Инженерная дисциплина
- Spec-Driven Development (`constraint-first-spec-generator`, `spec-test-linker`).
- Анти-бюрократия (`bureaucracy-detector`).
- RED-GREEN-REFACTOR цикл (`Superpowers`).
- Мутационное покрытие ≥85%.

---

## КОНТУР IV — ARIA INTERFACE (КОМАНДНЫЙ ЦЕНТР)

**Сверх-ядро:** `Aria-Interface-Hub` (Telegram-MCP, Interaction-Model, Visual-Insight, Dify-Visualizer, Excalidraw, CopilotKit).  
**HITL-арена** — многоканальный центр взаимодействия с фабрикой.

- Стриминг стратегических рассуждений `Aria-Cognitive-Core`.
- Тактические сводки от `Aria-Sentinel-Core` (PnL, маскировка, обнаруженные хищники).
- HITL-эскалация критических решений.
- Дашборды эффективности агентов и состояния капитала (`Visual-Insight`, `AntV`, `Excalidraw`).
- Интерактивные AI-интерфейсы и ко-агенты (`CopilotKit`).
- Визуальная оркестрация рабочих процессов (`Dify`, `LangFlow`, `n8n`).
- Голосовой и видео HITL (`RealChar`, `Fonoster`, `WhatsApp`, `OpenClaw`).
- Команды `/skill-find`, запросы на изменение тактик.

---

## КОНТУР V — CRYPTOGRAPHIC SECURITY (КВАНТОВО-УСТОЙЧИВАЯ ЗАЩИТА)

**Специализированный контур для криптографической защиты и приватности.**

- AES-256-GCM для шифрования всех конфигурационных файлов и памяти.
- RSA-2048/4096 + Kyber (постквантовая) для цифровой подписи обновлений.
- Zero-Knowledge Proofs (ZKP) для подтверждения прав на извлечение MEV.
- Multi-Party Computation (MPC) для распределённого управления ключами.
- Полная приватность данных: self-hosted Ollama, локальное выполнение, PII-редáкция.

---

## КОНТУР VI — AUTONOMOUS REPRODUCTION (АВТОНОМНОЕ ВОСПРОИЗВОДСТВО)

**Контур автономной эволюции кода и управления кодовой базой.**

- **Self-Modification Engine**: безопасная автономная модификация кода с трёх-рецензентским Blind Review Gate и откатом при деградации.
- **Swarm Coding Engine**: роевое кодирование (Kimi K2.6, Claude Code Swarm) с планами Plan-as-Code.
- **GitHub MCP**: полное управление репозиториями, PR, CI/CD, security scanning.
- **Spec Workflow MCP**: структурированная среда разработки на основе спецификаций.
- **Task Master**: AI-управление задачами с PRD-to-Task Pipeline.
- **Beads**: версионируемая графовая память задач (Dolt-powered).
- **kubefwd**: локальный мост к Kubernetes для отладки и разработки.

---

## КОНТУР VII — QUANTUM HUB (КВАНТОВЫЕ ВЫЧИСЛЕНИЯ — СТРАТЕГИЧЕСКИЙ РЕЗЕРВ)

**Резервный контур для квантово-ускоренных вычислений. Активируется при наличии квантового бэкенда.**

- **Quantum-Defender**: квантовый хаб (PennyLane, Qiskit, Julia/Yao).
- **Quantum-Synth**: квантовый синтез данных (LSTM-QGAN, Dual-PQC, Stylized-Facts QGAN).
- **Ising-Quantum-Bridge**: мост к квантовому превосходству (NVIDIA Ising).
- **Market-Hamiltonian-Estimator**: оценка гамильтониана рынка.
- Квантово-усиленная оценка риска (QAE) через `compute_quantum_var`.
- Квантовое решение линейных систем (HHL) для оптимизации портфеля.

---

> **Этот документ — живой. Каждое изменение фиксируется атомарным коммитом. ARIA Core и ARIA Trading разделены навсегда.**
