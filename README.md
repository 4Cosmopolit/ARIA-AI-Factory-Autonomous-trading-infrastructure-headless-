# ARIA-AI-Factory — Autonomous trading infrastructure

**Статус:** v.14.05.2026  
Полностью автономная MCP-сеть (30+ серверов), агентная память с эволюцией, контролируемое забывание, мутационное тестирование, self‑healing CI/CD, Telegram as MCP Arena.

---

## Ключевые файлы

| Файл | Назначение |
|------|------------|
| `AGENTS.md` | Инженерный контракт (дисциплина, жизненный цикл задачи) |
| `COGNITIVE.md` | Когнитивная архитектура, иерархия памяти, Palace Recall |
| `RULES.md` | Границы безопасности (always/never do) |
| `SKILLS.md` | Реестр навыков ARIA (150+) |
| `FACTORY_MEMORY.md` | 564+ инцидента, улучшивших систему |
| `SELF_REFERAT_NEW_CHAT.md` | Полный контекст для восстановления в новом чате |
| `CLAUDE.md` | Точка входа для ARIA |

---

## Активные рынки

- **Bybit** (бессрочные фьючерсы USDT‑M, спот)
- **Hyperliquid** (perps)
- **Арбитраж Bybit ↔ Binance**

### Замороженные рынки
Polymarket, Azuro, Zeitgeist (геоблокировка РФ)

---

## Требования

- Docker
- Python 3.10+
- Node.js 20+
- Git

---

## Быстрый старт

```bash
git clone https://github.com/4Cosmopolit/polymarket-orchestrator.git
cd polymarket-orchestrator
# Ознакомься с AGENTS.md, COGNITIVE.md, RULES.md
# Загрузи SELF_REFERAT_NEW_CHAT.md в новый чат для полного восстановления контекста



Теперь выполни в терминале:

```bash
git add README.md
git commit -m "ARIA-docs: обновлён README.md — ссылки на новые контракты и файлы"
git push origin main

