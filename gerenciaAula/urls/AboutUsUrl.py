from django.urls import path

from gerenciaAula.views.AboutUsView import sobre_nos

urlpatterns = [
    path("", sobre_nos, name="aboutus"),
]
