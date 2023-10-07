from django.shortcuts import render
from gerenciaAula.models import *
from gerenciaAula.views import *

def salvar_aula(request):
    print(request.POST, request.POST['disciplina'])

    # turmas = {'1': '1° Ano', '2': '2° Ano', '3': '3° Ano'}
    # turma = turmas[request.POST['cod_turma']]
    # lista_turmas = Turma.objects.get(nome_turma=turma).cod_turma?

    docente = Usuario.objects.get(user=request.user)

    if Aula.objects.last() is None:
        cont = 1
    else:
        cont = Aula.objects.last().cod_aula + 1

    aula = Aula.objects.create(
        cod_aula = cont,
        cod_hab = Habilidade.objects.get(cod_hab=request.POST['cod_hab']),
        cod_disc = Disciplina.objects.get(cod_disc=request.POST['disciplina']),
        desc_aula = request.POST['descricao'],
        user = Usuario.objects.get(user=docente.user),
        cod_turma = Turma.objects.get(cod_turma=request.POST['cod_turma']),
        fluxo_aula = request.POST['fluxo'],
        info_adicionais = request.POST['adicionais']
    )
    aula.save()

    # falta apenas saber onde serão salvas as informacões que será executada neste processo
    return render(request, 'aula-salva/aula-salva.html')