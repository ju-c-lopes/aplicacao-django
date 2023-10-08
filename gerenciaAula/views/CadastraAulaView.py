from django.shortcuts import render
from gerenciaAula.models import Habilidade, Turma, Disciplina
from gerenciaAula.views import *

def cadastrar_aula(request):
    
    codigos = Habilidade.objects.all().values()
    turmas = Turma.objects.all().values()
    disciplinas = Disciplina.objects.all()
    
    escolhas = None
    if request.method == 'POST':
        disciplina = Disciplina.objects.get(cod_disc=request.POST['disciplina'])
        
        escolhas = {
            'cod_hab': request.POST['habilidade'],
            'turma': request.POST['turma'],
            'disciplina': request.POST['disciplina'],
            'descricao': request.POST['descricao'],
        }

    dados = {
        'turmas': [t for t in turmas],
        'codigos': [c['cod_hab'] for c in codigos],
        'descricao': [x['desc_habilidade'] for x in codigos],
        'disciplinas': disciplinas,
    }
    
    if escolhas is not None and escolhas['cod_hab'] != '':
        dados['retorno'] = []
        for v in codigos:
            if v['cod_hab'] == escolhas['cod_hab']:
                escolha = {
                    'cod_hab': v['cod_hab'],
                    'turma': request.POST['turma'],
                    'disciplina': disciplina,
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
                    'disciplina': disciplina, 
                    'descricao': v['desc_habilidade'],
                }
                dados['retorno'].append(escolha)

    cont = 0
    
    user_agent = False
    if request.META['HTTP_USER_AGENT'].find('Android') != -1:
        user_agent = 'Android'
    elif request.META['HTTP_USER_AGENT'].find('iPhone') != -1:
        user_agent = 'Iphone'

    if escolhas is not None and len(dados['retorno']) >= 1:
        cont = len(dados['retorno'])
    dados['cont'] = cont
    dados['user_agent'] = user_agent

    return render(request, 'listagens/listagens.html', dados)