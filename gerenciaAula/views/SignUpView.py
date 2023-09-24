from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from gerenciaAula.views import *
from django.contrib import messages
from django.contrib.auth.models import User
from gerenciaAula.models import Usuario
from gerenciaAula.forms import RegistrationForm

def signup(request):

    form = RegistrationForm() 
    redirecionar = False
    message = None
    user_do_usuario = None

    if request.user.is_authenticated:
        logout(request)

    elif request.method == 'POST':

        # Este If/else fará um range a ser usado no próximo if
        if len(Usuario.objects.all()) == 0:
            cont = 0
        else:
            ultimo = Usuario.objects.last()
            cont = ultimo.id

        # este if criará um username automático com o primeiro nome
        # adicionado '-user' mais o range
        # Será necessário exibir ele após o cadastro
        if request.POST['nome'].find(' '):
            username = request.POST['nome'].split()[0].lower() + f'-user{cont + 1}'
        else:
            username = request.POST['nome'].lower + f'-user{cont + 1}'

        nome = request.POST['nome']
        nivel_usuario = int(request.POST['nivel_usuario'])
        eventual_doc = request.POST['eventual_doc']
        is_staff = True if nivel_usuario == 1 or nivel_usuario == 2 else False
        is_superuser = True if nivel_usuario == 1 else False

        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            password = request.POST['password1']
            print(password)

            usuario = User.objects.create_user(username=username, password=password, is_staff=is_staff, is_superuser=is_superuser)

            if usuario is not None:
                funcionario_usuario = Usuario.objects.filter(user__username=username).first()
                funcionario_usuario.nome = nome
                funcionario_usuario.nivel_usuario = nivel_usuario
                funcionario_usuario.eventual_doc = eventual_doc
                funcionario_usuario.save()

                message = {'type': 'success',  'text': 'Registration successful. You can now log in.'}
                user_do_usuario = funcionario_usuario.user
                print("eventual: ", funcionario_usuario.eventual_doc)
                redirecionar = True
            else:
                message = {'type': 'erro', 'text': 'Não foi possível cadastrar seu usuário.'}
        else:
            message = {'type': 'error',  'text': "There's an error on your form, check it."}
            form = RegistrationForm()
    
    context = {
        'usuario': user_do_usuario,
        'message': message,
        'form': form,
    }
    
    if redirecionar:
        url = reverse('login') + f"?usuario={context['usuario']}&message={context['message']['text']}&type={context['message']['type']}"
        return redirect(url)
    return render(request, 'signup/signup.html', context=context) 