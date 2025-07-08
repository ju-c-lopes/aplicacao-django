from django.urls import path

from gerenciaAula.views.MinhasAulasView import editar_aula, ver_aulas

urlpatterns = [
    path("", ver_aulas, name="ver-aulas"),
    path("editar-aula", editar_aula, name="editar-aula"),
]
