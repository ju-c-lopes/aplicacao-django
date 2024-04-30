from django.shortcuts import render
from gerenciaAula.views import *
from gerenciaAula.models import Aula, Usuario
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64
from django.http import HttpResponse
import csv

def addlabels(xaxis, yaxis):
    for i in range(len(xaxis)):
        plt.text(i, yaxis[i], yaxis[i])

def gerar_graficos(request):
    """
    Esta função é responsável por fazer o redirecionamento de qual gráfico será renderizado

    RETURN:
    -------
        - Retorna a renderização da página de acordo com o filtro que foi definido.
    """

    return_data, arquivos_csv = None, None

    if not request.POST:
        dados = gerar_grafico_padrao()
        return_data = dados[0]
        imagens_grafico = dados[1]
        arquivos_csv = dados[2]
        titulos = dados[3]
        id_analise = "padrão"
    elif request.POST.get("professor-analysis", None):
        teacher_list = request.POST.getlist("professor-selecionado", None)
        dados = gerar_grafico_professores(teacher_list)
        return_data = []
        imagens_grafico = []
        arquivos_csv = []
        titulos = []
        for dado in dados:
            return_data.append(dado[0])
            imagens_grafico.append(dado[1])
            arquivos_csv.append(dado[2])
            titulos.append(dado[3])
        id_analise = "prof"

    user_agent = False
    if request.META['HTTP_USER_AGENT'].find('Android') != -1:
        user_agent = 'Android'
    elif request.META['HTTP_USER_AGENT'].find('iPhone') != -1:
        user_agent = 'Iphone'

    context = {}
    context['charts'] = imagens_grafico
    context['professores'] = Usuario.objects.all()
    context['dados'] = return_data
    context['user_agent'] = user_agent
    context['csv_file'] = arquivos_csv
    context['titulos'] = titulos
    context['id_analise'] = id_analise

    return render(request, template_name='analises/analises.html', context=context, status=200)

# GRAFICO PADRÃO INICIAL

def gerar_grafico_padrao():
    """
    Esta função é responsável por recuperar os dados de todas as aulas.
    Então faz a contagem das habilidades que mais foram aplicadas.
    Ordena da habilidade mais aplicada para habilidade menos aplicada.
    Faz a construção dos dados a serem renderizados no gráfico e no csv.
    Constrói o arquivo csv e depois o gráfico matplotlib.

    RETURN
    ------
    tupla de listas para:
        1-) Dados para construção das tabelas
        2-) Gráficos
        3-) Arquivos CSV para serem baixados posteriormente
        4-) Título principal para o gráfico
    """
    aulas = [(aula.cod_hab.cod_hab, aula.cod_hab.desc_habilidade, aula.cod_hab.habilidade) for aula in Aula.objects.all()]
    habilidades = Counter([aula[0] for aula in aulas])
    
    titulo = [("Quantidade de Habilidades mais aplicadas",)]

    asc_hab = {hab: qtd for hab, qtd in sorted(habilidades.items(), key=lambda item: item[1], reverse=True)}
    print(asc_hab)

    asc_hab_list = list(asc_hab.items())
    asc_hab_list = asc_hab_list[:5]
    asc_hab_list = dict(asc_hab_list)

    desc_hab_list, todas_hab = {}, {}
    for aula in aulas:
        if aula[0] in habilidades.keys():
            todas_hab[f"{aula[0]}"] = {}
            todas_hab[f"{aula[0]}"]['cont'] = habilidades[f"{aula[0]}"]
            todas_hab[f"{aula[0]}"]['desc'] = aula[1]
            todas_hab[f"{aula[0]}"]['hab'] = aula[2]
        if aula[0] in asc_hab_list.keys():
            desc_hab_list[f"{aula[0]}"] = {}
            desc_hab_list[f"{aula[0]}"]['cont'] = asc_hab_list[f"{aula[0]}"]
            desc_hab_list[f"{aula[0]}"]['desc'] = aula[1]
            desc_hab_list[f"{aula[0]}"]['hab'] = aula[2]
    desc_hab_list = {k: v for k, v in sorted(desc_hab_list.items(), key=lambda item: item[1]["cont"], reverse=True)}
    todas_hab = {k: v for k, v in sorted(todas_hab.items(), key=lambda item: item[1]["cont"], reverse=True)}

    headers = ["Código da Habilidade", "Habilidade", "Descrição da Habilidade", "Quantidade"]
    arquivo_csv = salvar_csv(todas_hab, headers, 1)

    fig, ax = plt.subplots(dpi=150)
    bar_labels = list(asc_hab_list.keys())

    ax.bar(bar_labels, [value for value in asc_hab_list.values()])
    addlabels(bar_labels, [value for value in asc_hab_list.values()])
    ax.set_ylabel("Quantidade")
    ax.set_title("Habilidades aplicadas")
    plt.xticks(rotation=60)

    file_io = io.BytesIO()
    fig.savefig(file_io, bbox_inches='tight')
    b64 = base64.b64encode(file_io.getvalue()).decode()

    return ([desc_hab_list], [b64], [arquivo_csv.content.decode("utf-8")], titulo)

# GRÁFICO POR PROFESSORES

def gerar_grafico_professores(teacher_list):
    """
    Esta função recebe um dado de filtros em seu parâmetro.

    ARGS:
    -----
        :param teacher_list: Uma lista de professores que terão suas aulas analisadas.
    
    A função inicia com a abertura de uma lista para receber dados dos professores e das aulas que foram ministradas por eles.
    Faz a iteração armazenando os dados das aulas de cada um dos professores fornecidos no filtro.
    Filtra as aulas dadas por cada professor.
    Faz a associação da habilidade com a matéria lecionada.
    Faz a contagem das associações, elencando as mais aplicadas.
    """
    dados = []
    for i in range(len(teacher_list)):
        teacher_list[i] = Usuario.objects.get(user__username=teacher_list[i])
        aulas_dadas_pelo_professor = Aula.objects.filter(user=teacher_list[i].id)
        
        titulos = (f"Aulas dadas por {teacher_list[i].nome}", f"Total de aulas: {len(aulas_dadas_pelo_professor)}")
        
        qtd_aulas_dadas = []
        for aula in aulas_dadas_pelo_professor:
            habilidade_materia = f"{aula.cod_hab.cod_hab} | {aula.cod_disc.nome_disc}"
            qtd_aulas_dadas.append((habilidade_materia, aula.cod_hab.habilidade, aula.cod_hab.desc_habilidade, aula.user.nome))
            
        hab_mat = {hab: qtd for hab, qtd in sorted(Counter([aulas[0] for aulas in qtd_aulas_dadas]).items(), key=lambda item: item[1], reverse=True)}

        
        
        asc_hab_mat = list(hab_mat.items())
        asc_hab_mat = asc_hab_mat[:5]
        asc_hab_mat = dict(asc_hab_mat)

        aulas, todas_aulas = {}, {}
        for aula in qtd_aulas_dadas:
            if aula[0] in asc_hab_mat.keys():
                aulas[f"{aula[0]}"] = {}
                aulas[f"{aula[0]}"]["cont"] = asc_hab_mat[f"{aula[0]}"]
                aulas[f"{aula[0]}"]["habilidade"] = aula[1]
                aulas[f"{aula[0]}"]["desc"] = aula[2]
                aulas[f"{aula[0]}"]["prof"] = aula[3]
        aulas = {k: v for k, v in sorted(aulas.items(), key=lambda item: item[1]["cont"], reverse=True)}

        # qtd_aulas_dadas = {hab: qtd for hab, qtd in sorted(Counter([aulas[0] for aulas in qtd_aulas_dadas]).items(), key=lambda item: item[1], reverse=True)}
        # print(qtd_aulas_dadas)

        for aula in qtd_aulas_dadas:
            if aula[0] in hab_mat.keys():
                todas_aulas[f"{aula[0]}"] = {}
                todas_aulas[f"{aula[0]}"]["cont"] = hab_mat[f"{aula[0]}"]
                todas_aulas[f"{aula[0]}"]["habilidade"] = aula[1]
                todas_aulas[f"{aula[0]}"]["desc"] = aula[2]
                todas_aulas[f"{aula[0]}"]["prof"] = aula[3]
        print(todas_aulas)

        headers = ["Habilidade/Matéria", "Aulas Dadas", "Habilidade", "Descrição", "Professor(a)"]
        arquivo_csv = salvar_csv(todas_aulas, headers, 2)

        fig, ax = plt.subplots(dpi=150)
        bar_labels = list(asc_hab_mat.keys())

        ax.bar(bar_labels, [value for value in asc_hab_mat.values()])
        addlabels(bar_labels, [value for value in asc_hab_mat.values()])
        ax.set_ylabel("Quantidade")
        ax.set_title(f"Habilidades aplicadas por {teacher_list[i].nome}")
        plt.xticks(rotation=60)

        file_io = io.BytesIO()
        fig.savefig(file_io, bbox_inches='tight')
        b64 = base64.b64encode(file_io.getvalue()).decode()

        dados.append((aulas, b64, arquivo_csv.content.decode("utf-8"), titulos))
    
    return dados

def salvar_csv(dados_apresentados, headers, tipo):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="enter-your-filename.csv"'},
    )

    header_csv = headers

    writer = csv.writer(response)
    writer.writerow(header_csv)
    for k, v in dados_apresentados.items():
        if tipo == 1:
            line_csv = [f"{k}", f"{v['hab']}", f"{v['desc']}", f"{v['cont']}"]
        elif tipo == 2:
            line_csv = [f"{k}", f"{v['cont']}", f"{v['habilidade']}", f"{v['desc']}", f"{v['prof']}"]
        writer.writerow(line_csv)
    return response
