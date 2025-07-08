# Database Population Scripts

This project includes scripts to populate the Django database with initial data for Disciplinas, Turmas, and Habilidades.

## Files

-   `codigos-mysql-disciplinas.txt` - SQL script for Disciplinas (Subjects)
-   `codigos-mysql-turma.txt` - SQL script for Turmas (Classes)
-   `codigos-mysql-habilidades.txt` - SQL script for Habilidades (Skills)

## Usage Options

### 1. Django Management Command (Recommended)

```bash
# Basic usage
python manage.py init_db

# Force insertion (ignore duplicates)
python manage.py init_db --force
```

### 2. Standalone Shell Script

```bash
# Basic usage
./populate_db.sh

# Force insertion (ignore duplicates)
./populate_db.sh --force

# Use Django management command instead of direct SQL
./populate_db.sh --django-command

# Combined options
./populate_db.sh --force --django-command
```

### 3. Automatic Population

The database is automatically populated when running:

```bash
./build.sh
```

This script runs migrations and then calls `python manage.py init_db`.

## Data Overview

-   **Disciplinas**: 6 subjects (Matemática, Português, História, Geografia, Química, Física)
-   **Turmas**: 3 grade levels (1° Ano, 2° Ano, 3° Ano)
-   **Habilidades**: Educational skills with codes like EM13LGG101, EM13MAT101, etc.

## Notes

-   Scripts handle duplicate entries gracefully when using `--force` option
-   Database migrations must be run before population
-   SQLite database is located at `projeto/settings/db.sqlite3`
