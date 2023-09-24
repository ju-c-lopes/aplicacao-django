from django.shortcuts import render
from gerenciaAula.views import *
from gerenciaAula.models import Turma

def mais_info(request):
    print(request.POST)
    infos = {
        'cod_hab': request.GET['cod_hab'],
        'cod_turma': Turma.objects.get(cod_turma=request.GET['turma']).cod_turma,
        'turma': Turma.objects.get(cod_turma=request.GET['turma']).nome_turma,
        'disciplina': request.GET['disciplina'],
        'descricao': request.GET['descricao'],
    }
    return render(request, 'mais-info/mais-info.html', infos)