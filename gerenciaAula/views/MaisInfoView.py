from django.shortcuts import render
from gerenciaAula.views import *

def mais_info(request):
    infos = {
        'cod_hab': request.GET['cod_hab'],
        'turma': request.GET['turma'],
        'disciplina': request.GET['disciplina'],
        'descricao': request.GET['descricao'],
    }
    return render(request, 'mais-info.html', infos)