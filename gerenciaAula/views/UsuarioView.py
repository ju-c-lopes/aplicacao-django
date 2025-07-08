from django.shortcuts import render

from gerenciaAula.views import *


def list_usuario_view(request, id=None):
    if id is None and request.user.is_authenticated:
        id = request.user.id
    elif not request.user.is_authenticated:
        id = 0
    return render("<h1>Usuário de id %s!" % id)
