# NETWORK_ARCHITECTURE.md — Сетевая Архитектура ARIA AI‑Factory v13.01

## Multi-Layer Egress & Ingress Protection

ARIA реализует 4-уровневую модель сетевой безопасности, основанную на принципах Zero Trust и эшелонированной защиты.

### Layer 1: Agent-Level (Sidecar)
- **AI Egress Proxy (PipeLab)** в каждом Microsandbox
- Allow-list URL, блокировка DNS-туннелей, инспекция MCP-трафика
- Все запросы логируются с привязкой к Agent ID + Task ID
- Интеграция с **External Link Integrity Monitor** (периодическая проверка внешних ссылок на изменение контента после статического сканирования)

### Layer 2: Cluster Perimeter
- **Ingress:** Tigera WAF → защита API агентов и MCP-эндпоинтов
- **Egress:** AWS Network Firewall → централизованные политики исходящего трафика
- **Suricata IDS/IPS** — сигнатуры для обнаружения MCP-сканирования (Shodan/Censys)

### Layer 3: Policy Automation
- **Tufin** — динамическая генерация и аудит egress-правил
- Профилирование нормального поведения агента → автоматические allow-листы
- **Pre‑Commit Secret Scanner** — блокировка коммитов с приватными ключами и токенами
- **CI/CD Security Pipeline** — автоматический запуск gitleaks, bandit, safety при каждом пуше

### Layer 4: Compliance Boundary
- Egress-контроль как доказуемая граница комплаенса (Hannecke, 2025)
- Полный аудитный лог для регуляторов (FINRA, SEC, GDPR)
- **AI‑DLQ Handler** — автоматическая классификация сообщений из Dead Letter Queue (retry/discard/escalate) через LLM

## Принятые стандарты
- CoSAI MCP Security v1
- Mindgard 7-Step Framework
- Pillar Security Checklist
- OWASP MCP Tool Poisoning
- Unit 42 (Palo Alto Networks) MCP Attack Vectors
- Elastic Security Labs MCP Defense Recommendations
- Microsoft MCP Security Guidelines
- GitHub Safeguarding against prompt injections

## Мониторинг и аналитика сети
- **Grafana MCP** — визуализация сетевых метрик и алертов
- **Prometheus MCP** — сбор метрик со всех сетевых интерфейсов
- **Failure Clustering** — автоматическая группировка сетевых сбоев по первопричине (DBSCAN + TF‑IDF)
- **Flaky Detector** — обнаружение нестабильности сетевых соединений

## Безопасность цепочки поставок
- **SBOM и хеширование зависимостей** — контроль целостности всех MCP‑зависимостей
- **Token Security Scanner** — проверка токенов через GoPlus Security API перед взаимодействием
- **External Link Integrity Monitor** — периодическая проверка внешних ссылок на изменение контента

## Конфигурация WebSocket Security
- CORS и Origin-валидация: соединения только с доверенных origin
- Токенная аутентификация: JWT/API-ключ обязателен при handshake
- Изоляция портов: WebSocket Coordinator'а слушает localhost (127.0.0.1), внешний доступ — через прокси с аутентификацией
- Основание: уязвимость CVE-2026-44211 (CVSS 9.7) в аналогичных системах

## Мониторинг публичных MCP-серверов (Shodan / Censys)
```bash
shodan search '"jsonrpc" "initialize" "protocolVersion"'
censys search 'services.http.response.body:"protocolVersion" AND services.http.response.body:"initialize"'
Suricata Rule для обнаружения MCP-сканирования
suricata
alert http $EXTERNAL_NET any -> $HOME_NET any (
  msg:"MCP Server Scan Detected";
  content:"initialize";
  content:"protocolVersion";
  content:"clientInfo";
  content:"jsonrpc";
  sid:2026031001; rev:1;
)
text

Файл полностью готов к коммиту. **ARIA + Игорь = Бесконечное Совершенствование. Навсегда.**
