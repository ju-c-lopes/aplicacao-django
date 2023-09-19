from django.urls import path
from gerenciaAula.views.LogoutView import logout_user

urlpatterns = [
    path("", logout_user, name='logout'),
]

