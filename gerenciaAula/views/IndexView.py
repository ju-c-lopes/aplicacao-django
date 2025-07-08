from django.shortcuts import render

# from gerenciaAula.views import *


def index_view(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    return render(request, "index/index.html", status=200)
