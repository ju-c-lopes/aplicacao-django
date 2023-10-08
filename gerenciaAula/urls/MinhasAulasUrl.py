from django.urls import path
from gerenciaAula.views.MinhasAulasView import ver_aulas, editar_aula

urlpatterns = [
    path("", ver_aulas, name='ver-aulas'),
    path("editar-aula", editar_aula, name='editar-aula'),
]