from datetime import date

import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError

from gerenciaAula.models import Aula, Disciplina, Habilidade, Turma, Usuario


@pytest.mark.django_db
@pytest.mark.models
class TestDisciplinaModel:
    """Test cases for Disciplina model."""

    def test_create_disciplina(self):
        """Test creating a disciplina with valid data."""
        disciplina = Disciplina.objects.create(cod_disc="MAT", nome_disc="Matemática")

        assert disciplina.cod_disc == "MAT"
        assert disciplina.nome_disc == "Matemática"
        assert str(disciplina) == "Matemática"

    def test_disciplina_str_representation(self):
        """Test string representation of disciplina."""
        disciplina = Disciplina.objects.create(cod_disc="POR", nome_disc="Português")
        assert str(disciplina) == "Português"

    def test_disciplina_max_length_validation(self):
        """Test disciplina field max length validation."""
        # Test cod_disc max length (3 characters)
        with pytest.raises(Exception):  # Should raise validation error
            Disciplina.objects.create(
                cod_disc="MATH",  # 4 characters, exceeds max_length=3
                nome_disc="Matemática",
            )

    def test_disciplina_primary_key(self):
        """Test disciplina primary key uniqueness."""
        Disciplina.objects.create(cod_disc="FIS", nome_disc="Física")

        with pytest.raises(Exception):
            Disciplina.objects.create(cod_disc="FIS", nome_disc="Física 2")


@pytest.mark.django_db
@pytest.mark.models
class TestTurmaModel:
    """Test cases for Turma model."""

    def test_create_turma(self, disciplina):
        """Test creating a turma with valid data."""
        turma = Turma.objects.create(
            cod_turma=101, nome_turma="1° Ano A", cod_disc=disciplina
        )

        assert turma.cod_turma == 101
        assert turma.nome_turma == "1° Ano A"
        assert turma.cod_disc == disciplina
        assert str(turma) == "1° Ano A"

    def test_turma_str_representation(self, disciplina):
        """Test string representation of turma."""
        turma = Turma.objects.create(
            cod_turma=102, nome_turma="2° Ano B", cod_disc=disciplina
        )
        assert str(turma) == "2° Ano B"

    def test_turma_foreign_key_relationship(self, disciplina):
        """Test foreign key relationship with Disciplina."""
        turma = Turma.objects.create(
            cod_turma=103, nome_turma="3° Ano C", cod_disc=disciplina
        )
        assert turma.cod_disc.nome_disc == disciplina.nome_disc

    def test_turma_primary_key_uniqueness(self, disciplina):
        """Test turma primary key uniqueness."""
        Turma.objects.create(cod_turma=104, nome_turma="1° Ano A", cod_disc=disciplina)

        with pytest.raises(IntegrityError):
            Turma.objects.create(
                cod_turma=104,  # Duplicate primary key
                nome_turma="1° Ano B",
                cod_disc=disciplina,
            )


@pytest.mark.django_db
@pytest.mark.models
class TestHabilidadeModel:
    """Test cases for Habilidade model."""

    def test_create_habilidade(self):
        """Test creating a habilidade with valid data."""
        habilidade = Habilidade.objects.create(
            cod_hab="EF01MA01",
            habilidade="Utilizar números naturais",
            desc_habilidade="Utilizar números naturais como indicador de quantidade",
        )

        assert habilidade.cod_hab == "EF01MA01"
        assert habilidade.habilidade == "Utilizar números naturais"
        assert "números naturais" in habilidade.desc_habilidade
        assert str(habilidade) == "EF01MA01 | Utilizar números naturais"

    def test_habilidade_str_representation(self):
        """Test string representation of habilidade."""
        habilidade = Habilidade.objects.create(
            cod_hab="EF02POR01", habilidade="Leitura e interpretação"
        )
        assert str(habilidade) == "EF02POR01 | Leitura e interpretação"


@pytest.mark.django_db
@pytest.mark.models
class TestUsuarioModel:
    """Test cases for Usuario model."""

    def test_create_usuario_with_django_user(self, user_data):
        """Test creating usuario with Django User."""
        django_user = User.objects.create_user(**user_data)

        # Usuario should be created automatically via signal
        usuario = Usuario.objects.get(user=django_user)

        assert usuario.user == django_user
        assert usuario.nivel_usuario == 3  # Default is Docente
        assert str(usuario) == django_user.username

    def test_usuario_role_choices(self, create_user):
        """Test usuario role choices."""
        user = create_user()
        usuario = Usuario.objects.get(user=user)

        # Test default role
        assert usuario.nivel_usuario == 3  # Docente

        # Test changing roles
        usuario.nivel_usuario = 1  # Direção
        usuario.save()
        assert usuario.nivel_usuario == 1

        usuario.nivel_usuario = 2  # Coordenação
        usuario.save()
        assert usuario.nivel_usuario == 2

    def test_usuario_many_to_many_relationships(self, create_user, disciplina, turma):
        """Test many-to-many relationships with Disciplina and Turma."""
        user = create_user()
        usuario = Usuario.objects.get(user=user)

        # Test adding disciplina
        usuario.cod_disc.add(disciplina)
        assert disciplina in usuario.cod_disc.all()

        # Test adding turma
        usuario.cod_turma.add(turma)
        assert turma in usuario.cod_turma.all()

    def test_usuario_profile_creation_signal(self, django_user_model):
        """Test that Usuario profile is created automatically."""
        user = django_user_model.objects.create_user(
            username="signaltest", email="signal@test.com", password="TestPass123"
        )

        # Check that Usuario was created automatically
        assert Usuario.objects.filter(user=user).exists()

    def test_usuario_timestamps(self, create_user):
        """Test created_at and updated_at timestamps."""
        user = create_user()
        usuario = Usuario.objects.get(user=user)

        assert usuario.created_at == date.today()
        assert usuario.updated_at is not None


@pytest.mark.django_db
@pytest.mark.models
class TestAulaModel:
    """Test cases for Aula model."""

    def test_create_aula(self, teacher_user, disciplina, turma, habilidade):
        """Test creating an aula with all relationships."""
        usuario = Usuario.objects.get(user=teacher_user)

        aula = Aula.objects.create(
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

        assert aula.cod_aula == 1
        assert aula.tema_aula == "Números Naturais"
        assert aula.cod_hab == habilidade
        assert aula.user == usuario
        assert aula.cod_turma == turma
        assert aula.cod_disc == disciplina
        assert "livro didático" in aula.info_adicionais

    def test_aula_str_representation(self, aula):
        """Test string representation of aula."""
        expected = f"Aula de {aula.cod_disc.nome_disc} por {aula.user.nome}"
        assert str(aula) == expected

    def test_aula_foreign_key_relationships(self, aula):
        """Test all foreign key relationships."""
        assert aula.cod_hab.cod_hab is not None
        assert aula.user.user.username is not None
        assert aula.cod_turma.nome_turma is not None
        assert aula.cod_disc.nome_disc is not None

    def test_aula_timestamps(self, aula):
        """Test auto-generated timestamps."""
        assert aula.created_at == date.today()
        assert aula.updated_at is not None

    def test_aula_max_length_validation(
        self, teacher_user, disciplina, turma, habilidade
    ):
        """Test aula field max length validation."""
        usuario = Usuario.objects.get(user=teacher_user)

        # Test tema_aula max length (100 characters)
        long_tema = "A" * 101  # 101 characters

        with pytest.raises(Exception):
            aula = Aula(
                cod_aula=2,
                tema_aula=long_tema,
                user=usuario,
                cod_turma=turma,
                cod_disc=disciplina,
            )
            aula.full_clean()  # This will trigger validation

    def test_aula_optional_fields(self, teacher_user, disciplina, turma):
        """Test creating aula with only required fields."""
        usuario = Usuario.objects.get(user=teacher_user)

        aula = Aula.objects.create(
            cod_aula=3, user=usuario, cod_turma=turma, cod_disc=disciplina
        )

        assert aula.tema_aula is None
        assert aula.cod_hab is None
        assert aula.desc_aula is None
        assert aula.fluxo_aula is None
        assert aula.info_adicionais is None
