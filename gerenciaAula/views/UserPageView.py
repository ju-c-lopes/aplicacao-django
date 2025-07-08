from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from gerenciaAula.forms import EditUserForm, UserForm
from gerenciaAula.models import Usuario
from gerenciaAula.models.__init__ import ROLE_CHOICE
from gerenciaAula.views import *


def view_user(request, id=None):
    print(request)
    if id is None and request.user.is_authenticated:
        id = request.user.id
    elif not request.user.is_authenticated:
        id = 0
    context = {
        "role": ROLE_CHOICE[request.user.usuario.nivel_usuario - 1][1],
        "message": {
            "text": request.GET.get("message", None),
            "type": request.GET.get("type", None),
        },
    }
    return render(request, template_name="user-page/user-page.html", context=context)


def view_imagem(request, id=None):
    context = None
    if id is None and request.user.is_authenticated:
        id = request.user.id
        context = {"image": request.user.user__image}
    elif not request.user.is_authenticated:
        return render(request, template_name="<h1>Não há usuário</h1>")
    return render(request, template_name="user-page/user-page.html")


def edit_user(request):
    message = None
    username_sem_uso = True
    usuario = get_object_or_404(Usuario, user=request.user)
    user_usuario = get_object_or_404(User, id=request.user.id)

    form = EditUserForm(instance=usuario)
    user_form = UserForm(instance=request.user)

    if request.POST:
        form = EditUserForm(request.POST, request.FILES, instance=usuario)
        user_form = UserForm(request.POST, instance=request.user)
        verifica_username = (
            Usuario.objects.filter(user__username=request.POST["username"])
            .exclude(user__id=request.user.id)
            .first()
        )
        username_sem_uso = verifica_username is None

        if form.is_valid() and user_form.is_valid() and username_sem_uso:
            if request.POST["username"] is not None:
                user_usuario.username = request.POST["username"]
            user_usuario.save()

            if request.POST["nome"] is not None:
                usuario.nome = request.POST["nome"]
            if request.FILES and request.FILES["image"] is not None:
                usuario.image = request.FILES["image"]
            usuario.save()

            message = {
                "type": "success",
                "text": "Dados atualizados com sucesso.",
            }

            url = (
                reverse("usuario-view", args=(request.user.id,))
                + f"?message={message['text']}&type={message['type']}"
            )
            return redirect(url)

        else:
            if not username_sem_uso:
                message = {"type": "erro", "text": "Nome de usuário já está em uso."}
    else:
        if not username_sem_uso:
            message = {"type": "erro", "text": "Nome de usuário já está em uso."}

    context = {
        "message": message,
        "userForm": user_form,
        "usuarioForm": form,
    }

    return render(request, template_name="user-page/edit-user.html", context=context)
