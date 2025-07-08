import os

from django.core.management.base import BaseCommand
from django.db import connection

from projeto.settings.settings import BASE_DIR


class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais das tabelas Disciplina, Turma e Habilidade"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Força a inserção mesmo se houver conflitos (ignora duplicatas)",
        )

    def handle(self, *args, **kwargs):
        force = kwargs.get("force", False)

        # Arquivo SQL e suas descrições
        sql_files = [
            ("codigos-mysql-disciplinas.txt", "Disciplinas"),
            ("codigos-mysql-turma.txt", "Turmas"),
            ("codigos-mysql-habilidades.txt", "Habilidades"),
        ]

        self.stdout.write("🚀 Iniciando população do banco de dados...")

        for filename, description in sql_files:
            file_path = os.path.join(BASE_DIR, filename)

            if not os.path.exists(file_path):
                self.stdout.write(f"❌ ERRO: Arquivo não encontrado: {file_path}")
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    sql_script = file.read()

                with connection.cursor() as cursor:
                    # Split por statement se houver múltiplos INSERTs
                    statements = [
                        stmt.strip() for stmt in sql_script.split(";") if stmt.strip()
                    ]

                    for statement in statements:
                        try:
                            cursor.execute(statement)
                            self.stdout.write(f"✅ Executado: {statement[:50]}...")
                        except Exception as e:
                            if force:
                                self.stdout.write(
                                    f"⚠️ Aviso ao inserir {description}: {str(e)}"
                                )
                            else:
                                self.stdout.write(
                                    f"❌ Erro ao inserir {description}: {str(e)}"
                                )

                self.stdout.write(f"✅ {description} processadas com sucesso!")

            except Exception as e:
                self.stdout.write(f"❌ Erro ao processar {filename}: {str(e)}")

        # Mostra contadores finais
        self.show_counts()
        self.stdout.write("🎉 População do banco de dados concluída!")

    def show_counts(self):
        """Mostra contadores de registros inseridos"""
        try:
            with connection.cursor() as cursor:
                tables = [
                    ("Disciplina", "Disciplinas"),
                    ("Turma", "Turmas"),
                    ("Habilidade", "Habilidades"),
                ]

                self.stdout.write("\n📊 Contadores atuais:")
                for table_name, display_name in tables:
                    try:
                        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                        count = cursor.fetchone()[0]
                        self.stdout.write(f"  📋 {display_name}: {count} registros")
                    except Exception as e:
                        self.stdout.write(
                            f"  ❌ {display_name}: Erro ao contar - {str(e)}"
                        )
        except Exception as e:
            self.stdout.write(f"❌ Erro ao obter contadores: {str(e)}")
