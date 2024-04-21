from django.shortcuts import render
from gerenciaAula.views import *
from gerenciaAula.models.Aula import *
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64
from django.http import HttpResponse
import csv

def gerar_graficos(request):
    aulas = [(aula.cod_hab.cod_hab, aula.cod_hab.desc_habilidade, aula.cod_hab.habilidade) for aula in Aula.objects.all()]
    habilidades = Counter([aula[0] for aula in aulas])

    def addlabels(xaxis, yaxis):
        for i in range(len(xaxis)):
            plt.text(i, yaxis[i], yaxis[i])

    asc_hab = {hab: qtd for hab, qtd in sorted(habilidades.items(), key=lambda item: item[1], reverse=True)}

    asc_hab_list = list(asc_hab.items())
    asc_hab_list = asc_hab_list[:5]
    asc_hab_list = dict(asc_hab_list)

    desc_hab_list = {}
    for aula in aulas:
        if aula[0] in asc_hab_list.keys():
            desc_hab_list[f"{aula[0]}"] = {}
            desc_hab_list[f"{aula[0]}"]['cont'] = asc_hab_list[f"{aula[0]}"]
            desc_hab_list[f"{aula[0]}"]['desc'] = aula[1]
            desc_hab_list[f"{aula[0]}"]['hab'] = aula[2]
    desc_hab_list = {k: v for k, v in sorted(desc_hab_list.items(), key=lambda item: item[1]["cont"], reverse=True)}
    # for k, v in desc_hab_list.items():
    #     print("\n\nDESC Hab List KEY ==> ", k, "\n\tVALUE DESC ==> ", v)
    arquivo_csv = salvar_csv(desc_hab_list)

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
    context['habilidade'] = desc_hab_list
    context['user_agent'] = user_agent
    context['csv_file'] = arquivo_csv.content.decode("utf-8")

    return render(request, template_name='analises/analises.html', context=context, status=200)


def salvar_csv(dados_apresentados):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="enter-your-filename.csv"'},
    )

    header_csv = ["Código da Habilidade", "Habilidade", "Descrição da Habilidade", "Quantidade"]

    writer = csv.writer(response)
    writer.writerow(header_csv)
    for k, v in dados_apresentados.items():
        line_csv = [f"{k}", f"{v['hab']}", f"{v['desc']}", f"{v['cont']}"]
        writer.writerow(line_csv)
    return response
