from django.urls import path
from gerenciaAula.views.UserPageView import view_user, edit_user, view_imagem

urlpatterns = [
    path("<int:id>", view_user, name='usuario-view'),
    path("edit/", edit_user, name='usuario-edit'),
]
