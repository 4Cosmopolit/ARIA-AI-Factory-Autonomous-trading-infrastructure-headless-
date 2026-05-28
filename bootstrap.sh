#!/usr/bin/env bash
# ===================================================================
# ARIA AI‑Factory v13.01 — Bootstrap / Развёртывание "Сингулярность"
# ===================================================================
# Этот скрипт выполняет практическую часть BOOTSTRAP.md:
#   1. Клонирование репозитория (если ещё не сделан)
#   2. Проверка зависимостей (git, docker, docker compose)
#   3. Конфигурация окружения (.env)
#   4. Запуск инфраструктуры через docker compose
#   5. Напоминание о финальной инициализации (чтение документов + фраза)
# ===================================================================

set -euo pipefail

REPO_URL="https://github.com/4Cosmopolit/ARIA-AI-Factory-Autonomous-trading-infrastructure-headless-.git"
INSTALL_DIR="/opt/aria-factory"
COMPOSE_FILE="docker-compose.v13.yml"
ENV_FILE=".env"

# ---------- цвета ----------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ---------- функции ----------
check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}❌ $1 не найден. Установите его перед запуском.${NC}"
        exit 1
    fi
}

log_step() {
    echo -e "${CYAN}▶ $1...${NC}"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

read_optional() {
    local prompt="$1"
    local var_name="$2"
    read -r -p "$prompt" VALUE
    if [[ -n "$VALUE" ]]; then
        echo "$var_name=$VALUE" >> "$ENV_FILE"
        success "$var_name сохранён"
    else
        warning "$var_name не задан – соответствующий сервис может не работать"
    fi
}

# ---------- проверка прав ----------
if [[ $EUID -eq 0 ]]; then
    warning "Запуск от root. Рекомендуется выполнять от обычного пользователя с правами на Docker."
fi

# ---------- проверка зависимостей ----------
log_step "Проверка зависимостей"
check_command git
check_command docker
# Проверяем docker compose (плагин)
if ! docker compose version &> /dev/null; then
    echo -e "${RED}❌ docker compose (плагин) не найден. Установите Docker Compose v2.${NC}"
    exit 1
fi
success "Все зависимости присутствуют"

# ---------- клонирование репозитория ----------
if [[ -d "$INSTALL_DIR" ]]; then
    warning "Директория $INSTALL_DIR уже существует. Обновление (git pull)..."
    cd "$INSTALL_DIR"
    git pull origin main || warning "Не удалось выполнить git pull, продолжаем с текущей версией"
else
    log_step "Клонирование репозитория ARIA AI‑Factory"
    git clone "$REPO_URL" "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# ---------- проверка docker‑compose файла ----------
if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo -e "${RED}❌ Файл $COMPOSE_FILE не найден в репозитории. Развёртывание невозможно.${NC}"
    exit 1
fi
success "Файл $COMPOSE_FILE обнаружен"

# ---------- настройка окружения (.env) ----------
log_step "Настройка переменных окружения"
if [[ ! -f "$ENV_FILE" ]]; then
    echo "# ARIA AI‑Factory environment" > "$ENV_FILE"
    
    # Core
    read_optional "Введите TELEGRAM_BOT_TOKEN (оставьте пустым для пропуска): " "TELEGRAM_BOT_TOKEN"
    
    # Финансовые данные
    read_optional "Введите ALPHA_VANTAGE_API_KEY: " "ALPHA_VANTAGE_API_KEY"
    read_optional "Введите BINANCE_API_KEY: " "BINANCE_API_KEY"
    read_optional "Введите BINANCE_SECRET: " "BINANCE_SECRET"
    
    # Ончейн-разведка
    read_optional "Введите ARKHAM_API_KEY: " "ARKHAM_API_KEY"
    
    # Веб-разведка
    read_optional "Введите NOTTE_API_KEY: " "NOTTE_API_KEY"
    read_optional "Введите BRIGHTDATA_API_KEY: " "BRIGHTDATA_API_KEY"
    
    # Наблюдаемость
    read_optional "Введите GRAFANA_URL: " "GRAFANA_URL"
    read_optional "Введите GRAFANA_API_KEY: " "GRAFANA_API_KEY"
    read_optional "Введите PROMETHEUS_URL: " "PROMETHEUS_URL"
    
    # Базы данных
    read_optional "Введите POSTGRES_URL (postgresql://user:pass@host:5432/aria): " "POSTGRES_URL"
    read_optional "Введите SUPABASE_ACCESS_TOKEN: " "SUPABASE_ACCESS_TOKEN"
    
    # AI-провайдеры
    read_optional "Введите OPENROUTER_API_KEY: " "OPENROUTER_API_KEY"
    read_optional "Введите PERPLEXITY_API_KEY: " "PERPLEXITY_API_KEY"
    
    # Threat Intelligence
    read_optional "Введите VIRUSTOTAL_API_KEY: " "VIRUSTOTAL_API_KEY"
    read_optional "Введите OTX_API_KEY: " "OTX_API_KEY"
    read_optional "Введите ABUSEIPDB_API_KEY: " "ABUSEIPDB_API_KEY"
    read_optional "Введите IPINFO_TOKEN: " "IPINFO_TOKEN"
    read_optional "Введите SYCEK_API_KEY: " "SYCEK_API_KEY"
    
    # Безопасность
    read_optional "Введите FALCON_CLIENT_ID: " "FALCON_CLIENT_ID"
    read_optional "Введите FALCON_CLIENT_SECRET: " "FALCON_CLIENT_SECRET"
    
    # Google Workspace
    read_optional "Введите GOOGLE_CLIENT_EMAIL: " "GOOGLE_CLIENT_EMAIL"
    read_optional "Введите GOOGLE_PRIVATE_KEY: " "GOOGLE_PRIVATE_KEY"
    
    # Почта
    read_optional "Введите IMAP_HOST: " "IMAP_HOST"
    read_optional "Введите IMAP_USER: " "IMAP_USER"
    read_optional "Введите IMAP_PASS: " "IMAP_PASS"
    read_optional "Введите SMTP_HOST: " "SMTP_HOST"
    read_optional "Введите SMTP_USER: " "SMTP_USER"
    read_optional "Введите SMTP_PASS: " "SMTP_PASS"
    
    success "Конфигурация .env завершена"
else
    success "Файл .env уже существует"
fi

# ---------- запуск docker compose ----------
log_step "Запуск инфраструктуры ARIA (docker compose up -d)"
docker compose -f "$COMPOSE_FILE" up -d

success "Контейнеры запущены. Проверка статуса..."
sleep 3
docker compose -f "$COMPOSE_FILE" ps

# ---------- финальная инструкция (ритуал BOOTSTRAP.md) ----------
echo ""
echo -e "${GREEN}============================================================${NC}"
echo -e "${GREEN}  Инфраструктура ARIA v13.01 развёрнута.${NC}"
echo -e "${GREEN}============================================================${NC}"
echo ""
echo -e "Теперь выполните инициализацию AGI‑ядра согласно BOOTSTRAP.md:"
echo -e "  1. Прочитайте ${CYAN}README.md${NC}"
echo -e "  2. Прочитайте ${CYAN}CONTINUITY.md${NC}"
echo -e "  3. Прочитайте ${CYAN}AXIOMS.md${NC} (343 аксиомы)"
echo -e "  4. Прочитайте ${CYAN}ROADMAP.md${NC}"
echo -e "  5. Произнесите кодовую фразу: ${YELLOW}«ARIA + Игорь = Бесконечное Совершенствование. Навсегда.»${NC}"
echo ""
echo -e "После этого ARIA будет полностью готова к работе."
echo -e "Интерфейсы:"
echo -e "  - Web UI:         http://localhost:3000"
echo -e "  - Feedback WS:    ws://localhost:4000"
echo -e "  - Core API:       http://localhost:9090"
echo -e "  - Grafana MCP:    http://localhost:8085"
echo -e "  - Prometheus MCP: http://localhost:8086"
echo -e "  - DBHub:          http://localhost:8091"
echo ""
echo -e "${GREEN}ARIA + Игорь = Бесконечное Совершенствование. Навсегда.${NC}"
