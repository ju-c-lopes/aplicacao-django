from django.contrib.auth.models import User
from django.test import TestCase

from gerenciaAula.forms import LoginForm


class LoginFormTest(TestCase):
    def setUp(self):
        # Crie um usuário de teste e faça login
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_login_form_valid(self):
        # Dados de exemplo para preencher o formulário
        data = {
            "username": "testuser",
            "password": "testpassword",
        }

        # Crie uma instância do formulário com os dados
        form = LoginForm(data)

        # Verifique se o formulário é válido
        self.assertTrue(form.is_valid())

    def test_login_form_blank_fields(self):
        # Dados de exemplo com campos em branco
        data = {
            "username": "",
            "password": "",
        }

        form = LoginForm(data)

        # Verifique se o formulário é inválido devido a campos em branco
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("password", form.errors)
