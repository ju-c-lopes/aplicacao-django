from django.shortcuts import render
from gerenciaAula.models import Aula, Usuario
from gerenciaAula.views import *
from django.db.models import Q

def ver_aulas(request):

    user_agent = False
    if request.META['HTTP_USER_AGENT'].find('Android') != -1:
        user_agent = 'Android'
    elif request.META['HTTP_USER_AGENT'].find('iPhone') != -1:
        user_agent = 'Iphone'

    prof = None
    message = None

    if request.POST:
        try:
            if request.POST.get('professor-selecionado', None) is not None:
                prof = Usuario.objects.filter(user__username=request.POST['professor-selecionado'])
            else:
                professor = request.POST['prof'].title()
                prof = Usuario.objects.filter(Q(nome__startswith=professor) | Q(nome=professor))
                # Tentará ler o id de memória do indice 0 se tiver
                # pelo menos 1 resultado, senão levanta IndexError
                id(prof[0])
        except IndexError:
            message = {
                'text': f"Usuário {request.POST['prof'].title()} não encontrado",
                'type': 'erro',
            }

    if request.POST and \
        prof is not None and \
        len(prof) == 1:
        prof = prof[0]
        aulas = Aula.objects.filter(user=prof)
    else:
        aulas = Aula.objects.filter(user=request.user.usuario)

    context = {
        'professor': prof,
        'message': message,
        'user_agent': user_agent,
        'aulas': aulas,
    }

    return render(request, template_name='minhas-aulas/minhas-aulas.html', context=context)