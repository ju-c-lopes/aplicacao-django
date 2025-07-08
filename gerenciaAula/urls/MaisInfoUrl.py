from django.urls import path

from gerenciaAula.views.MaisInfoView import mais_info

urlpatterns = [
    path("", mais_info, name="mais-info"),
]
