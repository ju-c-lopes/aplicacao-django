from django.shortcuts import render
from gerenciaAula.views import *

def sobre_nos(request):
    return render(request, 'about-us/about-us.html')