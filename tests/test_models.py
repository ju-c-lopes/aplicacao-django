from django.test import TestCase

# from django.contrib.auth.models import User
from gerenciaAula.models import Disciplina, Turma


class TurmaModelTest(TestCase):
    def setUp(self):
        # Crie uma disciplina de teste
        self.disciplina = Disciplina.objects.create(nome_disc="Test Disciplina")

    def test_create_turma(self):
        # Crie um objeto Turma associado à disciplina de teste
        turma = Turma.objects.create(
            cod_turma=999,  # Defina o valor do campo primary_key de acordo com suas necessidades
            nome_turma="Test Turma",
            cod_disc=self.disciplina,
        )

        # Verifique se o objeto Turma foi criado corretamente
        self.assertEqual(turma.cod_turma, 999)  # Verifique o campo primary_key
        self.assertEqual(turma.nome_turma, "Test Turma")
        self.assertEqual(turma.cod_disc, self.disciplina)
