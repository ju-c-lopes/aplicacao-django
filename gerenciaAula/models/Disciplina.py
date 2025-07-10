from django.db import models
from django.forms import ValidationError


class Disciplina(models.Model):
    class Meta:
        db_table = "Disciplina"

    cod_disc = models.CharField(max_length=3, primary_key=True, default=0)
    nome_disc = models.CharField(max_length=45, blank=True, null=True)
    cod_aula = models.ForeignKey(
        "Aula", models.DO_NOTHING, db_column="cod_aula", blank=True, null=True
    )

    def clean(self):
        super().clean()
        if self.cod_disc and len(self.cod_disc) != 3:
            raise ValidationError({
                'cod_disc': 'O código da disciplina deve ter exatamente 3 caracteres.'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_disc}"
