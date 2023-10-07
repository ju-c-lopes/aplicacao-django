from django.urls import path
from gerenciaAula.views.MinhasAulasView import ver_aulas

urlpatterns = [
    path("", ver_aulas, name='ver-aulas'),
]