from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from gerenciaAula.models import Usuario


class EditUserForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ["nome", "image"]

        widgets = {
            "nome": forms.TextInput(),
            "image": forms.FileInput(),
        }


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ["username"]

        username = forms.TextInput()
