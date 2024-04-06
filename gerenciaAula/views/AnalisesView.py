from django.shortcuts import render
from gerenciaAula.views import *
from gerenciaAula.models.Aula import *
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io, base64

def gerar_graficos(request):
    aulas = [aula.cod_hab.cod_hab for aula in Aula.objects.all()]
    habilidades = Counter(aulas)

    def addlabels(xaxis, yaxis):
        for i in range(len(xaxis)):
            plt.text(i, yaxis[i], yaxis[i])

    asc_hab = {hab: qtd for hab, qtd in sorted(habilidades.items(), key=lambda item: item[1], reverse=True)}

    asc_hab_list = list(asc_hab.items())
    asc_hab_list = asc_hab_list[:5]
    asc_hab_list = dict(asc_hab_list)

    fig, ax = plt.subplots(dpi=150)
    bar_labels = list(asc_hab_list.keys())

    ax.bar(bar_labels, [value for value in asc_hab_list.values()])
    addlabels(bar_labels, [value for value in asc_hab_list.values()])
    ax.set_ylabel("Habilidades")
    ax.set_title("Habilidades aplicadas")
    plt.xticks(rotation=60)
    ax.set_ylim(0, 10)

    file_io = io.BytesIO()
    fig.savefig(file_io, bbox_inches='tight')
    b64 = base64.b64encode(file_io.getvalue()).decode()

    user_agent = False
    if request.META['HTTP_USER_AGENT'].find('Android') != -1:
        user_agent = 'Android'
    elif request.META['HTTP_USER_AGENT'].find('iPhone') != -1:
        user_agent = 'Iphone'

    context = {}
    context['chart'] = b64
    context['user_agent'] = user_agent

    return render(request, template_name='analises/analises.html', context=context, status=200)