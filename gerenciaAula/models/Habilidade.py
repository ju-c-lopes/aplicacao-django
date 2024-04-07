from gerenciaAula.models import *

class Habilidade(models.Model):
    cod_hab = models.CharField(primary_key=True, max_length=12)
    habilidade = models.CharField(max_length=60, blank=True, null=True)
    desc_habilidade = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cod_hab} | {self.habilidade}"

    class Meta:
        db_table = 'Habilidade'
