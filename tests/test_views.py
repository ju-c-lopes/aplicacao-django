from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LogoutUserViewTest(TestCase):
    def setUp(self):
        # Crie um usuário de teste e faça login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_logout_user(self):
        # Verifique se o usuário está autenticado
        self.assertTrue(self.user.is_authenticated)

        # Use reverse para obter a URL da view de logout
        url = reverse('logout')

        # Envie uma solicitação GET para a view de logout
        response = self.client.get(url)
        
        # Verifique se houve o redirecionamento
        self.assertEqual(response.status_code, 302)

        # Verifique se a resposta redireciona para a página inicial ('/')
        self.assertRedirects(response, '/')

    def tearDown(self):
        # Faça logout do usuário após o teste
        self.client.logout()

class IndexViewTest(TestCase):
    def test_index(self):
        # Use reverse para obter a URL da view
        url = reverse('home')
        response = self.client.get(url)

        # Verifique se a resposta é 200 (OK)
        self.assertEqual(response.status_code, 200)

