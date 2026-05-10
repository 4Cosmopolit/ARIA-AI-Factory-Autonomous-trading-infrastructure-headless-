# SKILLS.md — Реестр навыков ARIA

> **Версия:** 14.05.2026  
> **Формат:** стандарт Agent Skills (markdown с YAML-метаданными).  
> **Источники:** импортированные и адаптированные из `skills.sh`, Karpathy skills, Cowork skills, UI/UX Pro Max.

## Базовые must‑have скиллы (инцидент #482)

| Навык | Описание | Источник |
|-------|----------|----------|
| `superpowers` | Расширенные возможности Codex (автодополнение, рефакторинг) | Community |
| `task-master` | Декомпозиция задач, трекинг прогресса | Community |
| `browser-agent` | Управление браузером через Playwright (версия без MCP) | EdgeLab |
| `deep-research` | Глубокий поиск и синтез информации (NotebookLM) | EdgeLab |
| `memory-bank` | Работа с иерархической памятью (MemPalace) | MemPalace |

## Инженерные скиллы

| Навык | Описание |
|-------|----------|
| `spec-driven-development` | Генерация `SPEC.md`, `PLAN.md`, `EJECT_PLAN.md` |
| `tdd` | Обязательное написание тестов до реализации |
| `mutation-testing` | Запуск мутационного анализа через `validator-mcp` |
| `code-review-qa` | Пятистадийное ревью (static, QA, reasoning, multi-model, human) |
| `security-hardening` | Проверка на OWASP Top 10, CVE, supply chain |
| `vibelearning` | Обязательное объяснение изменений на естественном языке |

## Скиллы памяти

| Навык | Описание |
|-------|----------|
| `palace-recall` | Организация памяти по методу loci (Wing/Hall/Room) |
| `temporal-graph` | Работа с фактами, имеющими окна валидности |
| `memory-evolution` | Фоновый процесс перелинковки знаний (A-MEM) |
| `forgetting` | Контролируемое забывание, Nudge Engine, TTL |
| `mem0-hybrid` | Гибридный поиск (векторы + граф) |

## UI / дизайн скиллы

| Навык | Описание |
|-------|----------|
| `figma-intel` | Разведка через Figma MCP (анализ компонентов, токенов) |
| `claude-design-handoff` | Использование handoff bundle от Claude Design |
| `ui-forensics` | Анализ DOM, CSS, accessibility |
| `visual-explainer` | Визуализация отчётов (Mermaid, диаграммы) |

## Коммуникационные скиллы

| Навык | Описание |
|-------|----------|
| `telegram-arena` | Публичная координация агентов через Telegram |
| `guest-escallation` | Гостевой режим для эскалации HITL |
| `sse-streaming` | Стриминг рассуждений в реальном времени |

## Karpathy skills (инциденты #519–#521)

- `think-before-code` – обязательное планирование до реализации.
- `simplicity-first` – минимализм, удаление мёртвого кода.
- `scope-isolation` – изменения только в заданной области.
- `verified-minimal-solutions` – доказательства корректности, отсутствие «гибкости на будущее».

## Cowork skills (инциденты #486–#490)

- `inbox-processor` – автоматическая сортировка и приоритизация задач.
- `report-generator` – генерация структурированных отчётов для Risk Officer.
- `research-synthesizer` – синтез информации из множества источников.

## Импортированные из внешних реестров

- **UI/UX Pro Max** – 57 UI-стилей, 97 палитр, 57 шрифтовых пар.
- **Pencil** – MCP-холст для дизайна в IDE.
- **mct** – пакетный менеджер AI-контекста (версионирование `AGENTS.md`).
- **llm-cli** – унифицированный CLI для HITL.

---

**Все навыки доступны через `skills-registry-mcp` и команду `/skill-find` в Telegram.**

git add SKILLS.md
git commit -m "ARIA-core: добавлен SKILLS.md — реестр навыков ARIA"
git push origin main
