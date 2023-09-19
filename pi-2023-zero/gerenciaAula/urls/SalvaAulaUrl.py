from django.urls import path
from gerenciaAula.views.SalvaAulaView import salvar_aula

urlpatterns = [
    path("", salvar_aula, name='salvar-aula'),
]