from django.shortcuts import redirect
from django.contrib.auth import logout
from gerenciaAula.views import *

def logout_user(request):
    logout(request)
    return redirect('/')