# ARCHITECTURE.md — Архитектура ARIA AI‑Factory (v12.92)

## Обзор

ARIA AI‑Factory состоит из 40+ MCP-серверов, объединённых в 6 архитектурных контуров. Каждый контур решает свою задачу, а все вместе они образуют самодостаточную, автономную агентную экосистему.

## Контур I: Ядро и Память (Core & Memory)

| MCP-сервер | Назначение | Ключевые инструменты |
|:---|:---|:---|
| **temporal‑kg** | Динамический темпоральный граф знаний | `add_fact`, `search_episodes`, `get_entity_timeline` |
| **analytics‑mcp** | BPTT Auditor, Deflated Sharpe Ratio, Granger Causality | `bptt_audit`, `calculate_deflated_sharpe` |
| **bias‑firewall** | Защита от когнитивных искажений LLM | `detect_confirmation_bias`, `anti_sycophancy_check` |
| **ebm‑engine** | Энергетическая верификация утверждений | `ebm_score`, `ebm_rank`, `ebm_detect_hallucination` |
| **graphiti‑integration‑engine** | Динамический темпоральный граф знаний (Graphiti) | `add_fact`, `search_episodes`, `get_entity_timeline` |
| **cognee‑core‑engine** | Самообучающаяся память (ECL‑конвейер) | `cognee_remember`, `cognee_recall`, `cognee_improve` |
| **aria‑cognitive‑core** | Мозг ARIA: стратегическое мышление, прогнозирование | `deep_reasoning`, `macro_analysis`, `expert_panel` |
| **trinity‑reasoning‑engine** | Глубокий аналитический разум (замещается Deep Research Engine для исследовательских задач) | `deep_reasoning`, `investigate_incident`, `generate_strategic_plan` |
| **Macro Analyst** | Прогноз макро‑трендов | `macro_forecast`, `sentiment_analysis` |
| **deep‑research‑engine** | Автономное глубокое исследование | `deep_research`, `deep_research_parallel`, `deep_research_compare` |

## Контур II: Торговля и Охота (Trading & Hunting)

| MCP-сервер | Назначение | Ключевые инструменты |
|:---|:---|:---|
| **mev‑scanner** | Детекция MEV‑атак (Sandwich, JIT, FlashArb) | `scan_block`, `detect_sandwich`, `detect_jit` |
| **market‑maker‑hunter** | Детекция манипуляций (Spoofing, StopHunting, WashTrading) | `detect_spoof`, `detect_stop_hunt`, `detect_wash_trade` |
| **dispatch** | Исполнение ордеров с HITL‑блокировкой | `submit_order`, `preflight_check`, `execute_bundle` |
| **contest‑engine** | Внутренний конкурентный отбор стратегий | `compare_strategies`, `select_optimal`, `ensemble_vote` |
| **tradememory‑engine** | Специализированная торговая память (TradeMemory Protocol) | `tm_remember_trade`, `tm_preflight_check`, `tm_evolution_cycle` |
| **defi‑quant‑engine** | DeFi‑математика: AMM, MEV‑аукционы, Flashbots | `simulate_amm_swap`, `estimate_mev_profit`, `simulate_mev_auction` |
| **capital‑safety‑automation** | Автоматическая проверка безопасности капитала | `extract_counterparty_risk`, `evaluate_dynamic_limits`, `route_decision` |
| **compliance‑governor** | Регуляторный комплаенс (MiFID II, EU AI Act) | `compliance_export_mifid2`, `compliance_verify_integrity` |
| **quantdinger‑integration‑engine** | AI‑квантовая платформа | `quantdinger_ai_research`, `quantdinger_generate_strategy`, `quantdinger_backtest` |

## Контур III: CI/CD и Безопасность (CI/CD & Security)

| MCP-сервер | Назначение | Ключевые инструменты |
|:---|:---|:---|
| **sandbox‑mcp** | Изолированное выполнение кода (Docker, Git Worktrees, Microsandbox) | `sandbox_exec`, `docker_exec`, `git_worktree_create` |
| **overfit‑auditor** | Проверка на переобучение | `walk_forward_validation`, `sign_flip_ratio` |
| **crypto‑guardian** | Криптографическая защита (AES‑256‑GCM, RSA, Kyber) | `encrypt_document`, `verify_signature`, `rotate_keys` |
| **privacy‑guardian** | PII‑редáкция, локальное выполнение | `redact_pii`, `scan_for_secrets` |
| **agentic‑security‑engine** | SAST/DAST для агентных рабочих процессов | `agentic_sast_scan`, `agentic_dast_test`, `agentic_harden_prompts` |
| **zero‑trust‑policy‑engine** | Контроль внутренних запросов | `evaluate_internal_request`, `quarantine_agent` |
| **aidefence‑integration‑engine** | Трёхступенчатый Content Security Pipeline | `aidefence_pre_check`, `aidefence_process_check`, `aidefence_post_check` |
| **hexstrike‑integration‑engine** | Аудит смарт‑контрактов | `hexstrike_audit_contract`, `hexstrike_scan_code` |
| **misp‑integration‑engine** | Глобальная threat intelligence | `misp_search_ioc`, `misp_add_ioc`, `misp_search_cve` |
| **viper‑integration‑engine** | Проактивная имитация атак (Red Team) | `viper_start_assessment`, `viper_execute_module` |
| **ghidra‑integration‑engine** | Реверс‑инжиниринг бинарного кода (Ghidra) | `ghidra_decompile_function`, `ghidra_get_call_graph` |
| **enscan‑integration‑engine** | Китайский OSINT‑сенсор | `enscan_get_company_profile`, `enscan_get_investment_chain` |
| **microsandbox‑integration‑engine** | Аппаратно‑изолированные песочницы (KVM) | `microsandbox_create`, `microsandbox_run`, `microsandbox_exec` |
| **dagger‑integration‑engine** | MCP‑управление контейнерами и CI/CD | `dagger_run_container`, `dagger_build_and_test` |
| **kubefwd‑integration‑engine** | Локальный мост к Kubernetes | `kubefwd_start`, `kubefwd_status`, `kubefwd_get_logs` |

## Контур IV: Интерфейс и HITL (Interface & HITL)

| MCP-сервер | Назначение | Ключевые инструменты |
|:---|:---|:---|
| **telegram‑mcp** | Основной HITL‑канал (текст, голос, rich responses) | `send_message`, `send_visualization`, `voice_notify` |
| **interaction‑model‑engine** | Нативная мультимодальность, real‑time HITL | `stream_multimodal_context`, `real_time_collaborate` |
| **visual‑insight‑engine** | Диагностические графики и дашборды | `generate_diagnostic_views`, `detect_visual_anomaly` |
| **dify‑visualizer** | Визуализация RAG‑пайплайнов | `generate_visual_graph`, `record_decision_trace` |
| **openwebui‑integration‑engine** | Self‑hosted AI интерфейс | `openwebui_connect_model`, `openwebui_import_mcp_tools` |
| **dify‑integration‑engine** | Визуальная операционная система AI | `dify_create_app`, `dify_execute_workflow` |
| **langflow‑integration‑engine** | Визуальный AI‑конструктор | `langflow_create_flow`, `langflow_execute_flow` |
| **n8n‑integration‑engine** | Универсальная платформа автоматизации | `n8n_create_workflow`, `n8n_deploy_ai_agent` |
| **notebooklm‑integration‑engine** | Source‑grounded ответы с цитатами | `notebooklm_ask`, `notebooklm_verify_claim` |
| **pptagent‑integration‑engine** | Агентная среда генерации презентаций | `pptagent_generate_presentation`, `pptagent_evaluate_presentation` |
| **copilotkit‑integration‑engine** | Интерактивные AI‑интерфейсы и ко‑агенты | `copilotkit_deploy_ui_agent`, `copilotkit_generate_ui_component` |
| **lemonade‑integration‑engine** | Легковесный AI‑SDK для агентов | `lemonade_create_agent`, `lemonade_run_workflow` |
| **excalidraw‑integration‑engine** | Интерактивная визуальная доска | `excalidraw_create_element`, `excalidraw_export_to_svg` |
| **antv‑chart‑integration‑engine** | Специализированная визуализация данных | `antv_generate_chart`, `antv_auto_chart` |
| **drawio‑integration‑engine** | Генерация диаграмм на естественном языке | `diagram_generate`, `diagram_edit` |
| **talktofigma‑integration‑engine** | Полный контроль дизайна Figma через MCP | `talktofigma_create_ui_component`, `talktofigma_batch_update_texts` |
| **penpot‑integration‑engine** | Открытая дизайн‑платформа | `penpot_create_design_from_tokens`, `penpot_generate_ui_component` |
| **magic‑ui‑integration‑engine** | Мгновенная генерация UI‑компонентов | `magic_generate_component`, `magic_list_components` |
| **cad‑engine + godot‑integration‑engine** | 3D моделирование и визуализация | `cad_create_document`, `godot_create_scene` |
| **excel‑mcp‑integration‑engine** | Работа с финансовыми таблицами | `excel_create_workbook`, `excel_write_data` |
| **codeinterpreter‑integration‑engine** | Песочница для анализа данных | `codeinterpreter_run_analysis`, `codeinterpreter_generate_chart` |
| **whatsapp‑integration‑engine** | Коммуникационный мост к WhatsApp | `whatsapp_send_message`, `whatsapp_get_messages` |
| **fonoster‑integration‑engine** | Программируемые телекоммуникации | `fonoster_make_call`, `fonoster_handle_incoming_call` |
| **realchar‑integration‑engine** | Real‑time мультимодальный HITL | `realchar_start_session`, `realchar_speak` |
| **openclaw‑integration‑engine** | Персональный AI‑ассистент | `openclaw_send_message`, `openclaw_install_skill` |
| **hermes‑integration‑engine** | Self‑Evolving Agent | `hermes_run_task`, `hermes_learn_from_task` |

## Контур V: Квантовый Хаб (Quantum Hub) — Стратегический Резерв

| MCP-сервер | Назначение | Ключевые инструменты |
|:---|:---|:---|
| **quantum‑defender** | Квантовый хаб (PennyLane, Qiskit, Julia/Yao) | `qgan_generate`, `qcbm_generate`, `hhl_risk_solver` |
| **quantum‑synth** | Квантовый синтез данных (LSTM‑QGAN, Dual‑PQC, Stylized‑Facts) | `stylized_facts_qgan`, `lstm_qgan_generate` |
| **ising‑quantum‑bridge** | Мост к квантовому превосходству (NVIDIA Ising) | `ising_calibrate`, `ising_decode` |
| **market‑hamiltonian‑estimator** | Оценка гамильтониана рынка | `estimate_market_hamiltonian` |

## Контур VI: Автономное Воспроизводство (Autonomous Reproduction)

| MCP-сервер | Назначение | Ключевые инструменты |
|:---|:---|:---|
| **autonomous‑dev‑loop** | Генерация, тестирование и развёртывание кода агентами | `generate_code_from_spec`, `agent_factory`, `publish_plugin` |
| **swarm‑coding‑engine** | Роевое кодирование (Kimi K2.6, Claude Code Swarm) | `deploy_swarm`, `monitor_swarm_progress`, `merge_swarm_results` |
| **codebase‑knowledge‑engine** | Граф кодовой базы (GitNexus) | `query_impact`, `validate_mcp_contracts` |
| **self‑modification‑engine** | Безопасная автономная модификация кода | `self_analyze`, `self_design_improvement`, `self_execute_improvement` |
| **taskmaster‑integration‑engine** | AI‑управление задачами (Claude Task Master) | `taskmaster_parse_prd`, `taskmaster_analyze_complexity` |
| **github‑mcp‑integration‑engine** | Официальный GitHub MCP Server | `manage_repository`, `manage_pr`, `scan_security` |
| **gitmcp‑integration‑engine** | Живая документация (GitMCP) | `gitmcp_fetch_docs`, `gitmcp_verify_api` |
| **code2prompt‑integration‑engine** | Интеллектуальная подготовка контекста кодовой базы | `code2prompt_generate`, `code2prompt_get_tree` |
| **codex‑cli‑integration‑engine** | Терминальный MCP‑клиент и Sandbox | `codex_cli_execute`, `codex_cli_connect_mcp` |
| **desktop‑commander‑integration‑engine** | CLI‑интеграция и управление процессами | `dc_execute_command`, `dc_search_files`, `dc_edit_block` |
| **windows‑mcp‑integration‑engine** | Управление окнами и приложениями Windows | `win_launch_app`, `win_focus_app`, `win_screenshot_app` |
| **mobile‑mcp‑integration‑engine** | Универсальный мобильный сенсор и исполнительный канал | `mobile_list_devices`, `mobile_launch_app`, `mobile_list_elements` |
| **gemini‑cli‑integration‑engine** | Эталон агентной оркестрации (Gemini CLI) | `gemini_cli_query`, `gemini_cli_create_subagent` |
| **ollama‑integration‑engine** | Локальный LLM Runtime | `ollama_list_models`, `ollama_run`, `ollama_benchmark` |
| **fastmcp‑integration‑engine** | Высокоуровневый Python‑фреймворк для MCP | `fastmcp_create_server`, `fastmcp_add_tool` |
| **fastapi‑mcp‑integration‑engine** | Zero‑config адаптер FastAPI → MCP | `fastapi_mcp_mount`, `fastapi_mcp_secure` |
| **mcpo‑integration‑engine** | Универсальный MCP‑to‑OpenAPI прокси | `mcpo_proxy_server`, `mcpo_get_openapi_schema` |
| **klavis‑integration‑engine** | Универсальный MCP‑маршрутизатор и песочница | `klavis_create_strata`, `klavis_connect_oauth` |
| **mcp‑market‑integration‑engine** | Поиск, установка и управление MCP‑серверами | `mcp_market_search`, `mcp_market_install`, `mcp_market_audit_security` |
| **langroid‑integration‑engine** | Actor‑модель мультиагентной оркестрации | `langroid_create_actor_agent`, `langroid_run_task` |
| **fastagent‑integration‑engine** | Высокоуровневая операционная система для агентов | `fastagent_create_chain`, `fastagent_create_parallel` |
| **bifrost‑integration‑engine** | Высокопроизводительный AI‑шлюз | `bifrost_configure_provider`, `bifrost_set_fallback` |
| **higress‑integration‑engine** | AI‑Native API Gateway | `higress_route_model`, `higress_set_rate_limit` |
| **semantic‑cache‑engine** | Семантическое кэширование (Claude Context) | `semantic_cache_search`, `semantic_cache_store` |
| **semble‑integration‑engine** | Эффективное сжатие эмбеддингов | `semble_compress_embeddings`, `semble_get_optimal_dimension` |
| **vllm‑semantic‑router‑integration‑engine** | Сигнальный интеллектуальный маршрутизатор | `vllmsr_select_tools`, `vllmsr_filter_safety` |
| **notion‑integration‑engine** | Удалённый OAuth к Notion | `notion_search`, `notion_get_page`, `notion_create_page` |
| **atlassian‑integration‑engine** | Корпоративный мост к Atlassian (Jira/Confluence) | `atlassian_jira_search`, `atlassian_confluence_search` |
