from gerenciaAula.models import *

class Aula(models.Model):
    cod_aula = models.IntegerField(primary_key=True)
    tema_aula = models.CharField(max_length=100, blank=True, null=True)
    cod_hab = models.ForeignKey('Habilidade', models.DO_NOTHING, db_column='cod_hab', blank=True, null=True)
    desc_aula = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='user', blank=True, null=True)
    cod_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='cod_turma', blank=True, null=True)
    cod_disc = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='cod_disc', blank=True, null=True)
    fluxo_aula = models.CharField(max_length=500, blank=True, null=True)
    info_adicionais = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Aula'
