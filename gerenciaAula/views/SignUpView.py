from django.contrib.auth import logout
from django.shortcuts import render, redirect
from gerenciaAula.views import *
from django.contrib import messages
from gerenciaAula.models import Usuario
from gerenciaAula.forms import RegistrationForm, RegistrationUserForm

def signup(request):
    print(request.POST)
    form = RegistrationForm() #request.POST)
    # if request.user.is_authenticated:
    #     logout(request)

    # elif request.method == 'POST':
    #     print(request.POST)
    #     form = RegistrationForm(request.POST)
    #     print()
    #     print(form)
    #     print('Formulário é válido? ', form.is_valid())
    #     if form.is_valid():
    #         # if len(Usuario.objects.all()) == 0:
    #         #     cont = 0
    #         # else:
    #         #     ultimo = Usuario.objects.last()
    #         #     cont = ultimo.cod_doc
    #         # usuario = Usuario.objects.create(
    #         #     cod_doc = cont + 1,
    #         #     nome_doc = request.POST['nome'],
    #         #     eventual_doc = request.POST['is_temporary_teacher'],
    #         # )
    #         # usuario.save()
    #         # form.save()
    #         print('Tá válido!!!!!!!!!!!')
    #         messages.success(request, 'Registration successful. You can now log in.')
    #         return redirect('login')
    # else:
    #     # form = RegistrationForm()
    #     pass
    
    context = {
        'form': form,
    }

    print(context)

    print('renderizando......')
    
    return render(request, 'signup/signup.html', context=context) #{'form': form})