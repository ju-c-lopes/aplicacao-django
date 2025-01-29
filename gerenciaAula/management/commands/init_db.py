from django.core.management.base import BaseCommand
from django.db import connection
from projeto.settings.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Cria as tabelas do banco de dados com SQL customizado'

    def handle(self, *args, **kwargs):
        scripts = []
        files = [
            "disciplinas.txt",
            "habilidades.txt",
            "turma.txt",
        ]
        for i in range(3):
            with open(f"{BASE_DIR}/codigos-mysql-{files[i]}") as file:
                scripts.append(file.read())
        for sql_script in scripts:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql_script)
                except Exception:
                    continue
        self.stdout.write(self.style.SUCCESS('Tabelas criadas com sucesso!'))
