from django.urls import path

from gerenciaAula.views.CadastraAulaView import cadastrar_aula

urlpatterns = [
    path("", cadastrar_aula, name="cadastrar-aula"),
]
