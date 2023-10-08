from django.shortcuts import render, redirect
from gerenciaAula.models import Usuario
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from gerenciaAula.forms import LoginForm
from gerenciaAula.views import *

def login_user(request):
    context = None

    message = {
        'type': request.GET.get('type', None),
        'text': request.GET.get('message', None),
    }

    lembrar = request.POST.get('lembrar', False)
    nome_a_recordar = request.POST.get('nome', False)
    nome = None

    if lembrar and nome_a_recordar:
        nome = Usuario.objects.get(nome=nome_a_recordar).user
        lembrar = False
        message['type'] = 'success'

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            try:
                usuario = Usuario.objects.get(user__username=username)
                print(usuario)
                pass_user = check_password(password, usuario.user.password)
                user = authenticate(username=username, password=password)
                if user is not None and pass_user:
                    login(request, user)
                    return redirect('/')
                else:
                    message['text'] = f"Senha inválida."
                    message['type'] = 'erro'
            except:
                message['text'] = f"Usuário {username} não existe."
                message['type'] = 'erro'
                message['usuario_inv'] = True
        else:
            message['text'] = "Preencha o formulário corretamente."
            message['type'] = 'erro'
    else:
        form = LoginForm()
    
    context = {
        'usuario': request.GET.get('usuario', None) if nome is None else nome,
        'message': message,
        'lembrar': lembrar,
        'nome': nome,
    }
    return render(request, 'login/login.html', context=context, status=200)