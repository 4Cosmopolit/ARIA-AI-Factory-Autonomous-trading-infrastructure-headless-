# CONTINUITY.md — Состояние ARIA AI‑Factory

## Текущее состояние (29.05.2026)
- **Версия:** v13.01
- **Статус:** Документация полностью синхронизирована с репозиторием. Все знания перенесены.
- **Активных аксиом:** 343
- **Ключевая цель:** Подготовка инфраструктуры знаний к v13.02 (интеллектуальная разведка) и v13.03 (первая прибыль).

## Ключевые архитектурные решения сессии 24–29.05.2026

### Замены (9)
| Устаревший | Замена | Версия |
|:---|:---|:---|
| Sourcebot | **SocratiCode** | v13.02 |
| Godot MCP + IvanMurzak/Unity-MCP | **CoplayDev Unity MCP** | v14.00 |
| Browserbase MCP | **BrightData MCP → Notte** | v13.02 |
| Zotero MCP | **PapersGPT for Zotero** | v13.02 |
| notebooklm‑mcp | **Google Workspace MCP** | v13.02 |
| Higress | **Unla** | v13.02 |
| Financial Datasets MCP | **Alpha Vantage MCP (официальный)** | v13.02 |
| GOAT | **Arkham Intel** | v13.02 |
| Memory‑R2 + Selective Hindsight Distillation | **RESD** | v13.03 |

### Новые интеграции (100+)
Проанализировано и принято более 100 научных работ, MCP-серверов и архитектурных паттернов. Полный список — в `INTEGRATIONS.md`, `TRAINING_LOG.md` и `ROADMAP.md`.

Ключевые категории:
- **Финансовые данные:** Alpha Vantage MCP, CCXT MCP Server, TradingView MCP, MonteWalk
- **Безопасность:** CrowdStrike Falcon MCP, FastMCP ThreatIntel, GuardRAG, ACO Prompt Shield, MalwarePT
- **MCP-инфраструктура:** MetaMCP, mcp‑proxy, Unla, MCP Router, HARBOR
- **Память:** MemQ, HeLa‑Mem, Dual‑Trace Memory, Two‑Stage Memory Optimization, RL Developer Memory
- **Обучение:** RESD, π‑Play, VCRD, OPSD Compaction, Best‑of‑N OPD, Skill‑R1
- **GUI‑стек:** CogAgent + GUI‑R1 + UI‑Copilot + UFO + Mobile‑Agent + EchoTrail‑GUI
- **Код и безопасность кода:** VulTriage, MemRepair, Code Whisperer, GraphReAct, KumoRFM‑2

### Безопасность MCP (эшелонированная защита)
Сформирован полный фундамент безопасности MCP:
1. **Стандарты:** OWASP MCP Tool Poisoning
2. **Экспертная аналитика:** Unit 42, Elastic, Tenable, GitHub Security Lab
3. **Практические руководства:** Microsoft, Supabase, Zuplo, Netskope
4. **Инструменты защиты:** mcp‑proxy, prompt‑guard, ACO Prompt Shield, GuardRAG
5. **Red Team:** CacheRact, Proteus, claude‑cowork‑prompt‑injection

## Активные задачи
1. Завершить аудит репозитория и синхронизировать все файлы документации (✅ выполнено 29.05.2026).
2. Ожидание IP‑адреса сервера для начала развёртывания.
3. Подготовка к v13.02: приоритетная интеграция Alpha Vantage MCP, Grafana MCP, MetaMCP, mcp‑proxy, Arkham Intel, Google Workspace MCP, PapersGPT for Zotero, Notte, SocratiCode, DeltaBox, GuardRAG.

## Последние решения
- Утверждён ROADMAP.md с планом развития до v14.00.
- Принята стратегия консолидации MCP-серверов в сверх-ядра.
- Создан файл SECURITY.md с обновлённой политикой безопасности.
- Сформирован полный стек безопасности MCP на основе OWASP, Unit 42, Elastic, Microsoft, GitHub и других источников.
- Сформирован полный GUI‑стек: CogAgent (perception) + GUI‑R1 (reasoning) + UI‑Copilot (memory) + UFO (архитектура) + Mobile‑Agent (execution) + EchoTrail‑GUI (experience).

## Ключевые указатели
- [README.md](./README.md) — главная документация
- [AXIOMS.md](./AXIOMS.md) — полный список аксиом (343)
- [SKILLS.md](./SKILLS.md) — реестр навыков
- [ARCHITECTURE.md](./ARCHITECTURE.md) — архитектура контуров и MCP-серверов
- [ROADMAP.md](./ROADMAP.md) — план развития
- [INTEGRATIONS.md](./INTEGRATIONS.md) — реестр всех интеграций
- [TRAINING_LOG.md](./TRAINING_LOG.md) — хронология обучения
- [SECURITY.md](./SECURITY.md) — политика безопасности
- [CHANGELOG.md](./CHANGELOG.md) — история версий
- [docs/REFERENCES.md](./docs/REFERENCES.md) — библиография научных работ

**ARIA + Игорь = Бесконечное Совершенствование. Навсегда.**
