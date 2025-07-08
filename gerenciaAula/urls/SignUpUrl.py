from django.urls import path

from gerenciaAula.views.SignUpView import signup

urlpatterns = [
    path("", signup, name="signup"),
]
