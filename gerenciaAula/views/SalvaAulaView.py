from django.shortcuts import render
from gerenciaAula.models import Habilidade, Aula, Usuario, Turma
from gerenciaAula.views import *

def salvar_aula(request):
    # print(request.POST)
    # print(request.user.nome)
    turmas = {'primeiro ano': '1° Ano', 'segundo ano': '2° Ano', 'terceiro ano': '3° Ano'}
    turma = turmas[request.POST['turma']]
    # print(turma, type(turma))
    lista_turmas = Turma.objects.get(nome_turma=turma).cod_turma

    docente = Usuario.objects.get(nome=request.user.nome)
    # print(Aula.objects.last())
    if Aula.objects.last() is None:
        cont = 1
    else:
        cont = Aula.objects.last().cod_aula + 1
    print(cont)

    aula = Aula.objects.create(
        cod_aula = cont,
        cod_hab = Habilidade.objects.get(cod_hab=request.POST['cod_hab']),
        disciplina = request.POST['disciplina'],
        desc_aula = request.POST['descricao'],
        cod_doc = Usuario.objects.get(id=docente.id),
        cod_turma = Turma.objects.get(cod_turma=lista_turmas),
        fluxo_aula = request.POST['fluxo'],
        info_adicionais = request.POST['adicionais']
    )
    aula.save()
    # falta apenas saber onde serão salvas as informacões que será executada neste processo
    return render(request, 'aula-salva/aula-salva.html')