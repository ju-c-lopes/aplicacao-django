#!/bin/bash

# Simple test script to verify database path
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB_PATH="$PROJECT_DIR/projeto/settings/db.sqlite3"

echo "Project directory: $PROJECT_DIR"
echo "Database path: $DB_PATH"
echo "Database exists: $(test -f "$DB_PATH" && echo "YES" || echo "NO")"

if [ -f "$DB_PATH" ]; then
    echo "Database file size: $(stat -c%s "$DB_PATH") bytes"
    echo "Database permissions: $(stat -c%A "$DB_PATH")"
fi
