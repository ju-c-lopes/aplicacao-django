from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse

from gerenciaAula.models import Usuario, Aula, Habilidade


def ver_aulas(request):

    user_agent = False
    if request.META["HTTP_USER_AGENT"].find("Android") != -1:
        user_agent = "Android"
    elif request.META["HTTP_USER_AGENT"].find("iPhone") != -1:
        user_agent = "Iphone"

    prof = None
    message = None

    if request.POST:
        try:
            if request.POST.get("professor-selecionado", None) is not None:
                prof = Usuario.objects.filter(
                    user__username=request.POST["professor-selecionado"]
                )
            else:
                professor = request.POST["prof"].title()
                prof = Usuario.objects.filter(
                    Q(nome__startswith=professor) | Q(nome=professor)
                )
                # Tentará ler o id de memória do indice 0 se tiver
                # pelo menos 1 resultado, senão levanta IndexError
                id(prof[0])
        except IndexError:
            message = {
                "text": f"Usuário {request.POST['prof'].title()} não encontrado",
                "type": "erro",
            }

    if request.POST and prof is not None and len(prof) == 1:
        prof = prof[0]
        aulas = Aula.objects.filter(user=prof)
    else:
        aulas = Aula.objects.filter(user=request.user.usuario)

    context = {
        "professor": prof,
        "message": message,
        "user_agent": user_agent,
        "aulas": aulas,
    }

    return render(
        request, template_name="minhas-aulas/minhas-aulas.html", context=context
    )


def editar_aula(request):

    user_agent = False
    if request.META["HTTP_USER_AGENT"].find("Android") != -1:
        user_agent = "Android"
    elif request.META["HTTP_USER_AGENT"].find("iPhone") != -1:
        user_agent = "Iphone"

    aula = Aula.objects.get(cod_aula=request.POST["aula"])

    codigos = Habilidade.objects.all().values()
    retorno = []

    if request.POST.get("descricao", False):
        for v in codigos:
            if (
                request.POST["descricao"] != ""
                and request.POST["descricao"] in v["desc_habilidade"]
            ):
                escolha = {
                    "cod_hab": v["cod_hab"],
                    "descricao": v["desc_habilidade"],
                }
                retorno.append(escolha)

    hab = request.POST.get("habilidade", aula.cod_hab.cod_hab)
    fluxo = request.POST.get("fluxo", aula.fluxo_aula)
    info = request.POST.get("adicionais", aula.info_adicionais)

    if (
        aula.cod_hab.cod_hab != hab
        or aula.fluxo_aula != fluxo
        or aula.info_adicionais != info
    ):

        aula.cod_hab = (
            Habilidade.objects.get(cod_hab=hab) if aula.cod_hab != hab else aula.cod_hab
        )
        aula.desc_aula = (
            Habilidade.objects.get(cod_hab=hab).desc_habilidade
            if aula.cod_hab != hab
            else aula.desc_aula
        )
        aula.fluxo_aula = fluxo if aula.fluxo_aula != fluxo else aula.fluxo_aula
        aula.info_adicionais = (
            info if aula.info_adicionais != info else aula.info_adicionais
        )
        aula.save()

        url = reverse("salvar-aula") + "?updated=true"
        return redirect(url)

    context = {
        "cod_selected": request.POST.get("cod_selected", None),
        "retorno": retorno,
        "user_agent": user_agent,
        "cod_hab": codigos,
        "aula": aula,
    }

    return render(
        request, template_name="minhas-aulas/editar-aula.html", context=context
    )
