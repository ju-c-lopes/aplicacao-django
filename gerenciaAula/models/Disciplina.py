from gerenciaAula.models import *

class Disciplina(models.Model):
    
    cod_disc = models.CharField(max_length=3, primary_key=True, default=0)
    nome_disc = models.CharField(max_length=45, blank=True, null=True)
    cod_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='cod_aula', blank=True, null=True)

    def __str__(self):
        return f"{self.nome_disc}"

    class Meta:
        db_table = 'Disciplina'
