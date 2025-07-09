import pytest


@pytest.fixture
def client():
    """A Django test client instance."""
    from django.test import Client

    return Client()


@pytest.fixture
def django_user_model():
    """Django User model."""
    from django.contrib.auth.models import User

    return User


@pytest.fixture
def user_data():
    """Sample user data for testing."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "TestPass123#",
        "first_name": "Test",
        "last_name": "User",
    }


@pytest.fixture
def create_user(django_user_model, user_data):
    """Create a test user."""

    def _create_user(**kwargs):
        user_info = user_data.copy()
        user_info.update(kwargs)
        return django_user_model.objects.create_user(**user_info)

    return _create_user


@pytest.fixture
def teacher_user(create_user):
    """Create a teacher user with Usuario profile."""
    from gerenciaAula.models import Usuario

    user = create_user(username="teacher", email="teacher@example.com")
    usuario = Usuario.objects.get(user=user)
    usuario.nome = "Professor Teste"
    usuario.nivel_usuario = 3  # Docente
    usuario.save()
    return user


@pytest.fixture
def coordinator_user(create_user):
    """Create a coordinator user."""
    from gerenciaAula.models import Usuario

    user = create_user(username="coordinator", email="coordinator@example.com")
    usuario = Usuario.objects.get(user=user)
    usuario.nome = "Coordenador Teste"
    usuario.nivel_usuario = 2  # Coordenação
    usuario.save()
    return user


@pytest.fixture
def admin_user(create_user):
    """Create an admin user."""
    from gerenciaAula.models import Usuario

    user = create_user(username="admin", email="admin@example.com")
    usuario = Usuario.objects.get(user=user)
    usuario.nome = "Diretor Teste"
    usuario.nivel_usuario = 1  # Direção
    usuario.save()
    return user


@pytest.fixture
def disciplina():
    """Create a test disciplina."""
    from gerenciaAula.models import Disciplina

    return Disciplina.objects.create(cod_disc="MAT", nome_disc="Matemática")


@pytest.fixture
def turma(disciplina):
    """Create a test turma."""
    from gerenciaAula.models import Turma

    return Turma.objects.create(
        cod_turma=101, nome_turma="1° Ano A", cod_disc=disciplina
    )


@pytest.fixture
def habilidade():
    """Create a test habilidade."""
    from gerenciaAula.models import Habilidade

    return Habilidade.objects.create(
        cod_hab="EF01MA01",
        habilidade="Utilizar números naturais",
        desc_habilidade="Utilizar números naturais como indicador de quantidade",
    )


@pytest.fixture
def aula(teacher_user, disciplina, turma, habilidade):
    """Create a test aula."""
    from gerenciaAula.models import Aula, Usuario

    usuario = Usuario.objects.get(user=teacher_user)
    return Aula.objects.create(
        cod_aula=1,
        tema_aula="Números Naturais",
        cod_hab=habilidade,
        desc_aula="Aula sobre números naturais",
        user=usuario,
        cod_turma=turma,
        cod_disc=disciplina,
        fluxo_aula="Introdução, desenvolvimento, conclusão",
        info_adicionais="Material: livro didático",
    )


@pytest.fixture
def authenticated_client(client, teacher_user):
    """Client with authenticated teacher user."""
    client.force_login(teacher_user)
    return client


@pytest.fixture
def coordinator_client(client, coordinator_user):
    """Client with authenticated coordinator user."""
    client.force_login(coordinator_user)
    return client


@pytest.fixture
def admin_client(client, admin_user):
    """Client with authenticated admin user."""
    client.force_login(admin_user)
    return client
