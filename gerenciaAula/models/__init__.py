# Toda model (tabela) que for criada, deve ser incluida no arquivo
# __init__.py para que o django consiga enxergá-la de migrar no
# banco de dados

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, "Direçao"),
    (2, "Coordenação"),
    (3, "Docente"),
)

from .Aula import Aula
from .Disciplina import Disciplina
from .Habilidade import Habilidade
from .Turma import Turma
from .Usuario import Usuario
