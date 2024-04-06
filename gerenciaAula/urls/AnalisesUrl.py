from django.urls import path
from gerenciaAula.views.AnalisesView import gerar_graficos

urlpatterns = [
    path("", gerar_graficos, name='analises'),
]