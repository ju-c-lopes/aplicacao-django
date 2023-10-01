from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from gerenciaAula.views import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from gerenciaAula.models import Usuario, Disciplina, Turma
from gerenciaAula.forms import RegistrationForm

def signup(request):

    form = RegistrationForm() 
    redirecionar = False
    message = None
    user_do_usuario = None
    approved = False
    ROLE_CHOICE = (
        ('1', 'Direção'),
        ('2', 'Coordenação'),
        ('3', 'Docente'),
    )

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
        eventual_doc = False if request.POST['eventual_doc'] == 'False' else True
        
        subjects = request.POST.getlist('teached_subject')
        classes = request.POST.getlist('teached_classes')

        is_staff = True if nivel_usuario == 1 or nivel_usuario == 2 else False
        is_superuser = True if nivel_usuario == 1 else False

        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            password = request.POST['password1']

            aprovar = request.POST.get('aprovar', False)

            if aprovar:
                super = request.POST['super']
                superior = Usuario.objects.filter(user__username=super).first()
                pass_super = check_password(request.POST['pass-super'], superior.user.password)
                if (nivel_usuario == 1 or nivel_usuario == 2) and \
                    (superior.nivel_usuario == 1 and pass_super):
                    approved = True
                elif nivel_usuario == 3 and \
                    ((superior.nivel_usuario == 2 and pass_super) or \
                     (superior.nivel_usuario == 1 and pass_super)):
                    approved = True
            
            else:
                aprovar = True
                context = {
                    'aprovar': aprovar,
                    'nome': nome,
                    'nivel_usuario': nivel_usuario,
                    'eventual_doc': eventual_doc,
                    'password': password,
                    'role': ROLE_CHOICE[nivel_usuario - 1][0],
                    'rolename': ROLE_CHOICE[nivel_usuario - 1][1],
                    'form': form,
                    'subjects': subjects,
                    'classes': classes,
                }
                return render(request, 'signup/signup.html', context=context) 

            if approved:
                print("\nCriando usuario...\n")

                if subjects is not None:
                    subjects_cods = Disciplina.objects.filter(cod_disc__in=[x for x in subjects])
                
                if classes is not None:
                    classes_cods = Turma.objects.filter(cod_turma__in=[x for x in classes])

                usuario = User.objects.create_user(username=username, password=password, is_staff=is_staff, is_superuser=is_superuser)

                if usuario is not None:
                    funcionario_usuario = Usuario.objects.filter(user__username=username).first()
                    funcionario_usuario.nome = nome
                    funcionario_usuario.nivel_usuario = nivel_usuario
                    funcionario_usuario.eventual_doc = eventual_doc
                    for x in subjects_cods:
                        funcionario_usuario.cod_disc.add(x)
                    for x in classes_cods:
                        funcionario_usuario.cod_turma.add(x)
                    funcionario_usuario.save()

                    message = {'type': 'success',  'text': 'Cadastro feito com sucesso. Agora você pode fazer login.'}
                    user_do_usuario = funcionario_usuario.user
                    print("eventual: ", funcionario_usuario.eventual_doc)
                    redirecionar = True
                else:
                    message = {'type': 'erro', 'text': 'Não foi possível cadastrar seu usuário.'}
            else:
                message = {'type': 'erro', 'text': 'Não foi possível cadastrar seu usuário.'}
        else:
            message = {'type': 'erro',  'text': "Houve um erro no cadastro, verifique novamente."}
            form = RegistrationForm(request.POST)
    
    context = {
        'usuario': user_do_usuario,
        'message': message,
        'form': form,
    }
    
    if redirecionar:
        url = reverse('login') + f"?usuario={context['usuario']}&message={context['message']['text']}&type={context['message']['type']}"
        return redirect(url)
    return render(request, 'signup/signup.html', context=context) 