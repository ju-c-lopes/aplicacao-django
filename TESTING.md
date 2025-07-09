# Django Application Test Suite

This project includes a comprehensive test suite built with pytest and pytest-django.

## Test Structure

### Test Categories

-   **Models Tests** (`test_models.py`): Test all Django models, relationships, and validation
-   **Forms Tests** (`test_forms.py`): Test form validation, widgets, and data processing
-   **Views Tests** (`test_views.py`): Test view functionality, authentication, and responses
-   **URL Tests** (`test_urls.py`): Test URL routing, parameters, and access control
-   **Integration Tests** (`test_integration.py`): Test complete user workflows
-   **Password Tests** (`test password_force.py`): Test password validation logic

### Test Fixtures

Located in `tests/conftest.py`, providing:

-   User creation fixtures (teacher, coordinator, admin)
-   Model instance fixtures (disciplina, turma, habilidade, aula)
-   Authenticated clients for different user types

## Running Tests

### Prerequisites

```bash
# Install test dependencies
poetry install --with dev
# or
pip install pytest pytest-django pytest-cov
```

### Running All Tests

```bash
# Using poetry
poetry run pytest

# Using pip
pytest
```

### Running Specific Test Categories

```bash
# Model tests only
pytest -m models

# Form tests only
pytest -m forms

# View tests only
pytest -m views

# URL tests only
pytest -m urls

# Integration tests only
pytest -m integration

# Unit tests only
pytest -m unit
```

### Running with Coverage

```bash
pytest --cov=gerenciaAula --cov-report=html --cov-report=term-missing
```

### Using the Test Runner Script

```bash
./run_tests.sh
```

## Test Configuration

### Pytest Configuration (`pytest.ini`)

-   Uses Django settings: `projeto.settings.settings`
-   Optimized for performance with `--reuse-db` and `--nomigrations`
-   Includes coverage reporting
-   Custom markers for test categorization

### Django Test Settings

The settings file includes optimizations for testing:

-   In-memory SQLite database for faster tests
-   Disabled migrations
-   Simplified password hashing
-   Disabled logging during tests

## Test Examples

### Model Tests

```python
@pytest.mark.django_db
@pytest.mark.models
def test_create_aula(self, teacher_user, disciplina, turma, habilidade):
    # Test aula creation with all relationships
```

### Form Tests

```python
@pytest.mark.forms
def test_login_form_valid_data(self, create_user):
    # Test form validation with valid data
```

### View Tests

```python
@pytest.mark.django_db
@pytest.mark.views
def test_index_view_get(self, client):
    # Test view responses and permissions
```

### Integration Tests

```python
@pytest.mark.django_db
@pytest.mark.integration
def test_complete_user_registration_flow(self, client):
    # Test end-to-end user workflows
```

## Test Data and Fixtures

### User Types

-   **Teacher**: Basic user with teaching permissions
-   **Coordinator**: Mid-level user with broader access
-   **Admin**: Full access administrative user

### Model Instances

-   **Disciplina**: Subject/course (e.g., Mathematics)
-   **Turma**: Class/group (e.g., 1° Ano A)
-   **Habilidade**: Skill/competency (e.g., EF01MA01)
-   **Aula**: Lesson with all relationships

## Best Practices

1. **Use Markers**: Tag tests with appropriate markers (`@pytest.mark.models`)
2. **Use Fixtures**: Leverage conftest.py fixtures for consistent test data
3. **Test Isolation**: Each test should be independent
4. **Clear Naming**: Test names should clearly describe what they test
5. **Error Cases**: Test both success and failure scenarios
6. **Authentication**: Test both authenticated and anonymous access

## Continuous Integration

The test suite is designed to work well in CI/CD environments:

-   Fast execution with optimized settings
-   Clear output with pytest markers
-   Coverage reporting for code quality metrics
-   Isolated test database for parallel execution

## Coverage Goals

Current test coverage includes:

-   ✅ All model methods and relationships
-   ✅ Form validation and widgets
-   ✅ View authentication and responses
-   ✅ URL routing and access control
-   ✅ User workflows and integration
-   ✅ Password security validation

## Troubleshooting

### Common Issues

1. **ImportError**: Ensure `DJANGO_SETTINGS_MODULE` is set correctly
2. **Database Issues**: Use `--reuse-db` flag for faster execution
3. **Migration Errors**: Use `--nomigrations` for test optimization
4. **Coverage Issues**: Ensure all source code is in the coverage path

### Debug Mode

```bash
# Run with verbose output
pytest -v

# Run specific test with output
pytest tests/test_models.py::TestAulaModel::test_create_aula -v -s

# Run with pdb debugger
pytest --pdb tests/test_models.py
```
