from django.urls import path
from gerenciaAula.views.IndexView import index_view

urlpatterns = [
    path("", index_view, name='home'),
]