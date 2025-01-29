from django.shortcuts import render

from gerenciaAula.models import Disciplina, Turma
from gerenciaAula.views import *


def mais_info(request):

    user_agent = False
    if request.META["HTTP_USER_AGENT"].find("Android") != -1:
        user_agent = "Android"
    elif request.META["HTTP_USER_AGENT"].find("iPhone") != -1:
        user_agent = "Iphone"

    infos = {
        "user_agent": user_agent,
        "cod_hab": request.GET["cod_hab"],
        "cod_turma": Turma.objects.get(cod_turma=request.GET["turma"]).cod_turma,
        "turma": Turma.objects.get(cod_turma=request.GET["turma"]).nome_turma,
        "disciplina": Disciplina.objects.get(cod_disc=request.GET["disciplina"]),
        "descricao": request.GET["descricao"],
    }
    return render(request, "mais-info/mais-info.html", infos)
