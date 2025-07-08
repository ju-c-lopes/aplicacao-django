from gerenciaAula.models import *


class Turma(models.Model):
    class Meta:
        db_table = "Turma"

    cod_turma = models.IntegerField(primary_key=True)
    nome_turma = models.CharField(max_length=45, blank=True, null=True)
    cod_disc = models.ForeignKey(
        Disciplina, models.DO_NOTHING, db_column="cod_disc", blank=True, null=True
    )

    def __str__(self):
        return f"{self.nome_turma}"
