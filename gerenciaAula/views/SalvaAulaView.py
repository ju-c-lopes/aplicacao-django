from django.shortcuts import render

from gerenciaAula.models import Aula, Usuario, Habilidade, Disciplina, Turma


def salvar_aula(request):
    aula_user_teste = Aula.objects.filter(user=Usuario.objects.get(user=request.user))
    print(f"Len de aula: {len(aula_user_teste)}")
    if aula_user_teste[0].user.nome == "Usuário Teste" and len(aula_user_teste) >= 17:
        return render(request, "aula-limite-salvas/aula-atingida.html", status=403)

    docente = Usuario.objects.get(user=request.user)

    if Aula.objects.last() is None:
        cont = 1
    else:
        cont = Aula.objects.last().cod_aula + 1

    if request.GET.get("updated", None) != "true":
        aula = Aula.objects.create(
            cod_aula=cont,
            cod_hab=Habilidade.objects.get(cod_hab=request.POST["cod_hab"]),
            cod_disc=Disciplina.objects.get(cod_disc=request.POST["disciplina"]),
            desc_aula=request.POST["descricao"],
            user=Usuario.objects.get(user=docente.user),
            cod_turma=Turma.objects.get(cod_turma=request.POST["cod_turma"]),
            fluxo_aula=request.POST["fluxo"],
            info_adicionais=request.POST["adicionais"],
        )
        aula.save()

    return render(request, "aula-salva/aula-salva.html")
