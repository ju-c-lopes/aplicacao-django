from django.shortcuts import render
from gerenciaAula.models import Habilidade, Turma
from gerenciaAula.views import *

def cadastrar_aula(request):
    
    codigos = Habilidade.objects.all().values()
    escolhas = None
    if request.method == 'POST':
        escolhas = {
            'cod_hab': request.POST['habilidade'],
            # 'cod_turma': Turma.objects.get(cod_turma=)
            'turma': request.POST['turma'],
            'disciplina': request.POST['disciplina'],
            'descricao': request.POST['descricao'],
        }

    dados = {
        'codigos': [v['cod_hab'] for v in codigos],
        'descricao': [v['desc_habilidade'] for v in codigos],
    }
    if escolhas is not None and escolhas['cod_hab'] != '':
        dados['retorno'] = []
        for v in codigos:
            if v['cod_hab'] == escolhas['cod_hab']:
                escolha = {
                    'cod_hab': v['cod_hab'],
                    'turma': request.POST['turma'],
                    'disciplina': request.POST['disciplina'],
                    'descricao': v['desc_habilidade'],
                }
                dados['retorno'].append(escolha)
    else:
        dados['retorno'] = []
        for v in codigos:
            if escolhas is not None and \
                escolhas['descricao'] != '' and \
                escolhas['descricao'] in v['desc_habilidade']:
                escolha = {
                    'cod_hab': v['cod_hab'],
                    'turma': request.POST['turma'],
                    'disciplina': request.POST['disciplina'],
                    'descricao': v['desc_habilidade'],
                }
                dados['retorno'].append(escolha)
    cont = 0
    
    if escolhas is not None and len(dados['retorno']) >= 1:
        cont = len(dados['retorno'])
    dados['cont'] = cont

    return render(request, 'listagens/listagens.html', dados)