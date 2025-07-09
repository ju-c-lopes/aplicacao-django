#!/bin/bash
# Test runner script for the Django application

echo "=== Running Django Tests with Pytest ==="
echo ""

# Ensure we're in the project directory
cd "$(dirname "$0")"

# Activate poetry environment if using poetry
if command -v poetry &> /dev/null; then
    echo "Using Poetry environment..."
    poetry install --with dev
    
    # Run different test categories
    echo ""
    echo "Running all tests..."
    poetry run pytest
    
    echo ""
    echo "Running only model tests..."
    poetry run pytest -m models
    
    echo ""
    echo "Running only form tests..."
    poetry run pytest -m forms
    
    echo ""
    echo "Running only view tests..."
    poetry run pytest -m views
    
    echo ""
    echo "Running only URL tests..."
    poetry run pytest -m urls
    
    echo ""
    echo "Running integration tests..."
    poetry run pytest -m integration
    
    echo ""
    echo "Running with coverage report..."
    poetry run pytest --cov=gerenciaAula --cov-report=html --cov-report=term-missing
    
else
    echo "Poetry not found. Using pip environment..."
    
    # Install requirements
    pip install -r requirements.txt
    pip install pytest pytest-django pytest-cov
    
    # Run tests
    pytest
fi

echo ""
echo "=== Test execution completed ==="
echo "Coverage report available in htmlcov/index.html"
