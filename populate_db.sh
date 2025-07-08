#!/bin/bash

# Database population script for Django application
# This script runs SQL scripts to populate the SQLite database after migrations
# 
# Usage: ./populate_db.sh [--force] [--django-command]
#   --force: Ignore duplicate entry errors and continue
#   --django-command: Use Django management command instead of direct SQL

# Set variables
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB_PATH="$PROJECT_DIR/projeto/settings/db.sqlite3"
MANAGE_PY="$PROJECT_DIR/manage.py"

# Parse arguments
FORCE=false
USE_DJANGO=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --force)
            FORCE=true
            shift
            ;;
        --django-command)
            USE_DJANGO=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--force] [--django-command]"
            echo "  --force: Ignore duplicate entry errors and continue"
            echo "  --django-command: Use Django management command instead of direct SQL"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Django Database Population Script ===${NC}"
echo -e "${BLUE}Project directory: $PROJECT_DIR${NC}"
echo -e "${BLUE}Database path: $DB_PATH${NC}"

# Check if manage.py exists
if [ ! -f "$MANAGE_PY" ]; then
    echo -e "${RED}Error: manage.py not found at $MANAGE_PY${NC}"
    exit 1
fi

# Check if settings directory exists
SETTINGS_DIR="$PROJECT_DIR/projeto/settings"
if [ ! -d "$SETTINGS_DIR" ]; then
    echo -e "${RED}Error: Settings directory not found at $SETTINGS_DIR${NC}"
    echo -e "${YELLOW}Available directories in projeto/:${NC}"
    ls -la "$PROJECT_DIR/projeto/" 2>/dev/null || echo "projeto/ directory not found"
    exit 1
fi

# Change to project directory
cd "$PROJECT_DIR"

# Use Django management command if requested
if [ "$USE_DJANGO" = true ]; then
    echo -e "${BLUE}Using Django management command...${NC}"
    if [ "$FORCE" = true ]; then
        python manage.py init_db --force
    else
        python manage.py init_db
    fi
    exit $?
fi

echo -e "${BLUE}Database path: $DB_PATH${NC}"

# Check if database file exists
if [ ! -f "$DB_PATH" ]; then
    echo -e "${YELLOW}Warning: Database file not found at $DB_PATH${NC}"
    echo -e "${YELLOW}Running migrations to create database...${NC}"
    python manage.py migrate
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error: Failed to run migrations${NC}"
        exit 1
    fi
    echo -e "${GREEN}Migrations completed successfully${NC}"
    
    # Verify database was created
    if [ ! -f "$DB_PATH" ]; then
        echo -e "${RED}Error: Database file still not found after migrations${NC}"
        echo -e "${YELLOW}Expected location: $DB_PATH${NC}"
        echo -e "${YELLOW}Available files in settings directory:${NC}"
        ls -la "$PROJECT_DIR/projeto/settings/" 2>/dev/null || echo "Settings directory not accessible"
        exit 1
    fi
else
    echo -e "${GREEN}Database file found at: $DB_PATH${NC}"
fi

echo -e "${BLUE}Starting database population...${NC}"

# Function to execute SQL and handle errors
execute_sql() {
    local sql_file="$1"
    local description="$2"
    
    echo -e "${YELLOW}Populating $description...${NC}"
    
    if [ ! -f "$sql_file" ]; then
        echo -e "${RED}Error: SQL file not found: $sql_file${NC}"
        return 1
    fi
    
    # Use sqlite3 to execute the SQL file
    if [ "$FORCE" = true ]; then
        # Create a modified SQL that ignores conflicts
        temp_sql=$(mktemp)
        sed 's/INSERT INTO/INSERT OR IGNORE INTO/g' "$sql_file" > "$temp_sql"
        sqlite3 "$DB_PATH" < "$temp_sql"
        result=$?
        rm "$temp_sql"
    else
        sqlite3 "$DB_PATH" < "$sql_file"
        result=$?
    fi
    
    if [ $result -eq 0 ]; then
        echo -e "${GREEN}✓ $description populated successfully${NC}"
        return 0
    else
        if [ "$FORCE" = true ]; then
            echo -e "${YELLOW}⚠ Warning: Some issues occurred while populating $description (possibly duplicate entries)${NC}"
            return 0
        else
            echo -e "${RED}✗ Error populating $description${NC}"
            return 1
        fi
    fi
}

# Execute SQL scripts in the correct order (dependencies first)

# 1. Populate Disciplinas (no dependencies)
execute_sql "$PROJECT_DIR/codigos-mysql-disciplinas.txt" "Disciplinas"

# 2. Populate Turmas (no dependencies)
execute_sql "$PROJECT_DIR/codigos-mysql-turma.txt" "Turmas"

# 3. Populate Habilidades (no dependencies)
execute_sql "$PROJECT_DIR/codigos-mysql-habilidades.txt" "Habilidades"

echo -e "${GREEN}=== Database population completed! ===${NC}"

# Optional: Show counts of inserted records
echo -e "${BLUE}Current record counts:${NC}"
sqlite3 "$DB_PATH" "SELECT 'Disciplinas: ' || COUNT(*) FROM Disciplina;" 2>/dev/null || echo "  Disciplinas: Table not found"
sqlite3 "$DB_PATH" "SELECT 'Turmas: ' || COUNT(*) FROM Turma;" 2>/dev/null || echo "  Turmas: Table not found"
sqlite3 "$DB_PATH" "SELECT 'Habilidades: ' || COUNT(*) FROM Habilidade;" 2>/dev/null || echo "  Habilidades: Table not found"

echo -e "${GREEN}Database population script finished successfully!${NC}"
echo -e "${BLUE}Tip: Use '--django-command' to use Django's management command instead${NC}"
