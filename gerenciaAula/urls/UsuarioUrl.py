from django.urls import path

from gerenciaAula.views.UsuarioView import list_usuario_view

urlpatterns = [
    path("", list_usuario_view, name="usuario"),
    path("<int:id>", list_usuario_view, name="usuario"),
]
