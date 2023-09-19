from gerenciaAula.models import *

class Habilidade(models.Model):
    cod_hab = models.CharField(primary_key=True, max_length=12)
    habilidade = models.CharField(max_length=60, blank=True, null=True)
    desc_habilidade = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Habilidade'
