from django import forms
from django.forms import ModelForm
from gerenciaAula.models import Usuario
from django.contrib.auth.models import User

class EditUserForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome', 'image']

        widgets = {
            'nome': forms.TextInput(),
            'image': forms.FileInput(),
        }

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username']
    
        username = forms.TextInput()