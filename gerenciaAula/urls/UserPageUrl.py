from django.urls import path

from gerenciaAula.views.UserPageView import edit_user, view_imagem, view_user

urlpatterns = [
    path("<int:id>", view_user, name="usuario-view"),
    path("edit/", edit_user, name="usuario-edit"),
]
