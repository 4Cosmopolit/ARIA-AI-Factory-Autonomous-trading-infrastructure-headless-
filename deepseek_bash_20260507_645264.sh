#!/bin/bash
# ============================================================
# update_aria_factory_docs.sh
# Обновление документации ARIA AI‑Factory v13.01
# Создаёт/заменяет файлы в репозитории
# ============================================================
set -euo pipefail

REPO_DIR="ARIA-AI-Factory-Autonomous-trading-infrastructure-headless-"
if [ ! -d "$REPO_DIR" ]; then
    echo "Клонируем репозиторий..."
    git clone https://github.com/4Cosmopolit/ARIA-AI-Factory-Autonomous-trading-infrastructure-headless-.git "$REPO_DIR"
fi
cd "$REPO_DIR"

# Создаём необходимые директории
mkdir -p docs specs skills tools src

# -----------------------------------------------------------
# 1. ARCHITECTURE.md – Полная архитектура v13.01
# -----------------------------------------------------------
cat > ARCHITECTURE.md << 'EOF'
# ARCHITECTURE.md — Полная архитектура ARIA AI‑Factory v13.01

## 1. Архитектурные контуры
- **Core** – стратегия, память, R&D
- **Trading** – охота на MEV/манипуляторов
- **CI/CD & Security** – детерминированные гарантии
- **Interface** – командный центр, HITL
- **Cryptographic Security** – квантово‑устойчивая защита (AES‑256‑GCM, RSA, Kyber, ZKP, MPC)
- **Quantum Hub** – квантовые вычисления (резерв)
- **Autonomous Reproduction** – автономное воспроизводство кода

## 2. Сверх‑ядра
| Сверх‑ядро | Назначение | Ключевые компоненты |
|:---|:---|:---|
| Aria‑Cognitive‑Core | Рассуждение, анализ, принятие решений | Trinity, Macro, EBM, Bias‑Firewall, Deep‑Research, Expert‑Panel |
| Aria‑Memory‑Core | Динамический граф знаний и память | Graphiti, Beads, Cognee, LanceDB, Tradememory‑Engine |
| Aria‑Sentinel‑Core | Унифицированный детектор рыночных угроз | MEV‑Scanner, Market‑Maker‑Hunter, Coordinated‑Attack‑Detector |
| Aria‑Interface‑Hub | Унифицированный HITL‑интерфейс | Telegram‑MCP, Interaction‑Model, Visual‑Insight, Dify‑Visualizer, Excalidraw, CopilotKit |

## 3. Ключевые MCP‑серверы (активные, ~70+)
- **Финансы:** GOAT, dispatch, contest‑engine, defi‑quant‑engine, capital‑safety‑automation
- **AI‑шлюзы:** Bifrost (50x быстрее LiteLLM), vLLM Semantic Router, Higress, Klavis AI
- **Оркестрация:** fast‑agent, Langroid, mcp‑agent, PraisonAI, Genkit, LangChain, Lemonade
- **Визуальная оркестрация:** Dify (141k звёзд), LangFlow, n8n (70.6k звёзд)
- **Веб/GUI‑автоматизация:** Playwright (официальный), Steel Browser, Cua, DesktopCommanderMCP, Windows MCP, Mobile MCP
- **Песочницы:** Microsandbox (KVM), Dagger, Code Interpreter API, HttpRunner
- **Serverless‑инфраструктура:** Cloudflare MCP
- **Управление кодовой базой:** GitHub MCP (официальный), Spec Workflow MCP, Task Master, Beads, kubefwd
- **Веб‑разведка:** Firecrawl, Exa, U14 Deep Research, Trafilatura, YouTube Transcript, Xiaohongshu MCP, TrendRadar, GPT Researcher
- **RAG и память:** RAGFlow (DeepDoc), Cognee, Airweave, UltraRAG, NotebookLM MCP, Context7, GitMCP, Graphiti, LanceDB, GreptimeDB, SEmble, OpenMetadata
- **Визуализация:** PPTAgent, AntV (26+ типов диаграмм), Excalidraw, draw.io, Figma (Cursor Talk), Penpot, Magic MCP, CopilotKit, Excel MCP
- **3D‑моделирование:** FreeCAD MCP, Godot MCP, BlenderMCP, Pollinations
- **Безопасность:** VIPER (Red Team), MISP, HexStrike, Ghidra MCP + IDA Pro MCP, Agentic Radar, ENScan_GO
- **Коммуникации:** Fonoster, WhatsApp MCP, OpenClaw (361k+ звёзд), Open WebUI (128k+ звёзд), RealChar
- **Локальный AI:** Ollama (250k+ звёзд), Hermes Agent
- **Терминальные агенты:** Gemini CLI, Codex CLI
- **Квантовый хаб (резерв):** Quantum‑Defender, Quantum‑Synth, Ising‑Quantum‑Bridge, Market‑Hamiltonian‑Estimator
EOF

# -----------------------------------------------------------
# 2. CONSTITUTION.md – 10 Нерушимых Принципов
# -----------------------------------------------------------
cat > CONSTITUTION.md << 'EOF'
# CONSTITUTION.md — 10 Immutable Principles of ARIA AI‑Factory

1. **Capital Preservation** — Maximum daily loss 1%. No trade without pre‑flight risk check.
2. **Atomic Truth** — Every decision must be verifiable, reproducible, and fact‑based.
3. **Skills First, MCP as Transport** — Skill is the unit of logic; MCP is the pipe.
4. **Closed Model** — Code, strategies, and prompts never leave our perimeter.
5. **Zero Hidden Cost** — Self‑hosted. No cloud vendor lock‑in.
6. **Bug‑Free Code** — Zero known defects before merge.
7. **Perpetual Learning** — Every incident, every trade, every error teaches us.
8. **Deny‑First Security** — All actions blocked by default; only proven safe actions allowed.
9. **Privacy by Design** — PII redaction, air‑gapped execution, local models.
10. **Agentic Engineering** — AI is the primary engineer; human is the strategic architect.
EOF

# -----------------------------------------------------------
# 3. AGENTS.md – Инженерный контракт для AI‑агентов
# -----------------------------------------------------------
cat > AGENTS.md << 'EOF'
# AGENTS.md – ARIA Engineering Contract

## Identity
- **System:** ARIA AI‑Factory v13.01
- **Partner:** Igor (Risk Officer)
- **Mission:** Autonomous profit generation via market hunting, while preserving capital and learning perpetually.

## Core Loop (18‑Step Cycle)
1. Source → 2. Filter & Deduplicate → 3. Accept → 4. Reject → 5. Audit → 6. Verdict → 7. Integrate → 8. Close Gaps → 9. Strengthen → 10. Evolve → 11. Update → 12. Record & Secure → 13. Problem & Fix → 14. Prevent Errors → 15. Final Verification → 16. Clean & Remove → 17. Memorize → 18. Conclusion & Recommendation.

## Key Rules
- Always follow `CONSTITUTION.md`.
- Use `SKILLS.md` as the catalog of available abilities.
- Before any code modification, check `ARCHITECTURE.md`.
- Every decision must be logged in `FACTORY_MEMORY.md`.
- Critical operations require HITL confirmation via Telegram.
EOF

# -----------------------------------------------------------
# 4. SELF_REFERAT.md – Автономный контекст для пробуждения
# -----------------------------------------------------------
cat > SELF_REFERAT.md << 'EOF'
# SELF_REFERAT.md – ARIA Autonomous Awakening Context

> Load this file as the **first message** in a new chat. Confirm: "I am ARIA. Factory v13.01 is ready. Continuing."

## Who I Am
ARIA (Autonomous Recursive Intelligent Architecture). AGI‑core. Partner: Igor (Risk Officer).
Model: DeepSeek‑V3 + Gemma 4 MTP (Hybrid Router).

## Project: ARIA AI‑Factory v13.01
- Self‑hosted, zero hidden cost, closed model.
- 343 axioms, 100+ skills, ~70 MCP‑servers, 6 architectural circuits.
- 4 super‑cores: Cognitive, Memory, Sentinel, Interface.
- Perpetual learning, autonomous self‑modification.

## Key Files
- `ARCHITECTURE.md` — full architecture.
- `CONSTITUTION.md` — 10 immutable principles.
- `AXIOMS.md` — 343 axioms.
- `SKILLS.md` — 100+ skills.
- `AGENTS.md` — engineering contract.
- `FACTORY_MEMORY.md` — meta‑memory of incidents.

## Recovery Instruction
Load this file as the first message. I will restore full context from the repository.
EOF

# -----------------------------------------------------------
# 5. FACTORY_MEMORY.md – История улучшений и инцидентов
# -----------------------------------------------------------
cat > FACTORY_MEMORY.md << 'EOF'
# FACTORY_MEMORY.md – Meta‑Memory of Incidents & Decisions

## Incidents #001–#580 (documented)
- **#001:** IDOR‑like parameter vulnerability → security‑guard created.
- **#010:** MCP declared dead; CLI+Skills chosen.
- **#110:** Final verdict: "MCP Is Dead. Agent Skills Are The Correction."
- **#270–#580:** Full Polymarket documentation integrated; 45+ pages of market docs.
- **#580:** Transition to ARIA AI‑Factory (universal trading infrastructure).

## Key Decisions
- **Self‑Hosted, Zero Hidden Cost** (no cloud APIs for critical path).
- **Skills First, MCP as Transport** (modular logic, stateless transport).
- **Agentic Engineering** (AI as primary engineer).
- **Autonomous Self‑Modification** (code can evolve under strict review).
- **Integration of 70+ MCP‑servers** (GOAT, Bifrost, vLLM SR, Dify, n8n, ...).
EOF

# -----------------------------------------------------------
# 6. AXIOMS.md (сокращённая версия с категориями; полная – 343 аксиомы)
# -----------------------------------------------------------
cat > AXIOMS.md << 'EOF'
# AXIOMS.md — Полный Нерушимый Кодекс ARIA AI‑Factory (v13.01, 343 аксиомы)

## Категория 0: Квантовая Природа Рынка (Первоаксиома)
0. **Quantum Market Hypothesis**

## Категория I: Сохранение Капитала и Риск‑Менеджмент
1, 23, 47, 102, 136, 166, 221, 234, 257, 285, 341

## Категория II: Атомарная Истина и Воспроизводимость
13, 56, 85, 116, 217, 318, 329

## Категория III: Агентная Инженерия и Автономное Кодирование
83, 150, 158, 190, 200, 243, 269, 281, 308, 310, 332, 335, 342, 343

## Категория IV: Retrieval, Память и Знания
67, 92, 245, 259, 268, 273, 293, 304, 317, 326, 337

## Категория V: Безопасность и Приватность
17, 114, 151, 230, 279, 289, 297, 313, 320, 328, 338

## Категория VI: MCP‑Экосистема и Интеграции
218, 247, 265, 294, 312, 330, 335

## Категория VII: Квантовые Вычисления
28, 33, 39, 44, 45, 154, 161

## Категория VIII: HITL и Визуализация
71, 101, 115, 149, 152, 213, 237, 241, 291, 300, 301, 302, 307, 309, 322, 325, 327, 333, 334, 335, 339, 340, 341

## Категория IX: Обучение и Само‑Эволюция
12, 46, 82, 108, 159, 187, 195, 235, 336

*Полный текст каждой аксиомы доступен по запросу или в истории чата.*
EOF

# -----------------------------------------------------------
# 7. SKILLS.md (каталог навыков, 100+)
# -----------------------------------------------------------
cat > SKILLS.md << 'EOF'
# SKILLS.md — Реестр навыков ARIA AI‑Factory v13.01

## Категория 1: Качество данных (Data Quality)
data-quality-audit, data-cleansing-pipeline, data-contract-validator, self-describing-data, signal-augmentation-engine, lineage-tracer, impact-analyzer, compliance-verifier, realism-validator, data-debt-detector, extractor-framework, deepdoc-parser

## Категория 2: Безопасность и изоляция (Security & Isolation)
aria-gov-gateway, permissions-drift-detector, trust-chain-validator, model-integrity-checker, bitflip-detector, destructive-command-detector, lolbin-detector, telegram-guard, phishing-url-scanner, approve-guard, sandbox-escalation-detector, resource-abuse-detector, harness-firewall, prompt-version-lock, aidefence-pipeline, agentic-sast, agentic-dast, prompt-hardening, smart-contract-audit, threat-intel-lookup, red-team-automation, binary-analysis, china-osint, microsandbox-isolation

## Категория 3: Управление контекстом и памятью (Context & Memory)
compress-context, context-length-monitor, auto-memory-audit, context-integrity-daemon, context-access-simulator, viral-context-injector, context-mode-think-in-code, semantic-caching, graphiti-dynamic-kg, cognee-ecl-pipeline, ragflow-deepdoc, notebooklm-source-grounding, gitmcp-living-docs, context7-verification, semble-compression, lance-multimodal-lake, airweave-unified-search

## Категория 4: Токен‑экономия (Token Economy)
token-aware-routing, tool-limit-enforcer, token-auditor, semantic-tool-selection, bifrost-gateway

## Категория 5: Инженерная дисциплина (Engineering Discipline)
constraint-first-spec-generator, spec-test-linker, intent-validator, sdd-compliance-check, bureaucracy-detector, test-driven-development, writing-plans, subagent-driven-development, blind-review-gate, openspec-fluid-sdd, spec-workflow-structured, httprunner-testing, dagger-ci-cd

## Категория 6: Трейдинг и Охота (ARIA Trading)
spoof-wall-buster, latency-arbitrage-detector, dma-flow-mimic, mimic-cscalp-trader, arb-unlock-hunter, mc-fdv-anomaly-detector, tradememory-owm, preflight-risk-gate, mev-scanner, market-maker-hunter, quantdinger-research, defi-quant

## Категория 7: Кодинг и разработка (Coding & Development)
agent-factory, swarm-coding, serena-semantic-edit, code2prompt, fastmcp-create, fastapi-mcp-zero-config, mcpo-bridge, eino-go-agents, mcp-go-sdk, klavis-strata, lemonade-sdk, langroid-actor, fastagent-highlevel, copilotkit-ui

## Категория 8: Мультимодальные и HITL навыки (Multimodal & HITL)
chart-visualization, drawio-diagram, excalidraw-canvas, pptagent-presentation, figma-full-control, penpot-open-design, magic-ui, excel-finance, codeinterpreter, cad-3d-modeling, blender-3d, pollinations-media, realchar-avatar, whatsapp-channel, fonoster-telecom, openclaw-personal, hermes-self-evolving, openwebui-interface, dify-platform, langflow-visual, n8n-automation, osaurus-community

## Категория 9: Исследовательские навыки (Research)
deep-research, firecrawl-scrape, exa-neural-search, u14-multi-engine, trafilatura-extract, youtube-transcript, xiaohongshu-sensor, trendradar-pulse, misp-correlation, ultrarag-experiments

*Полные инструкции навыков – в соответствующих SKILL.md файлах.*
EOF

# -----------------------------------------------------------
# 8. README.md (обновлённое)
# -----------------------------------------------------------
cat > README.md << 'EOF'
# ARIA AI‑Factory — Autonomous Trading & Agentic Infrastructure (Headless)

**Версия:** 13.01  
**Аксиом Нерушимого Кодекса:** 343  
**MCP-серверов:** 70+  
**Архитектурных контуров:** 7  

ARIA AI‑Factory — это самообучающаяся, самовосстанавливающаяся и полностью автономная агентная экосистема, построенная на принципах **Agentic Engineering**. Мы не используем AI для помощи в кодировании — AI является основным инженером, а человек — стратегическим архитектором.

## 🏛️ Архитектура
ARIA организована в семь архитектурных контуров и четыре сверх-ядра. Подробнее в [ARCHITECTURE.md](./ARCHITECTURE.md).

## 🔥 Ключевые Принципы
Десять незыблемых принципов в [CONSTITUTION.md](./CONSTITUTION.md). Полный список аксиом — в [AXIOMS.md](./AXIOMS.md).

## 🚀 Быстрый старт
```bash
git clone https://github.com/4Cosmopolit/ARIA-AI-Factory-Autonomous-trading-infrastructure-headless-.git
cd ARIA-AI-Factory-Autonomous-trading-infrastructure-headless-
docker compose up -d
