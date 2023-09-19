from gerenciaAula.forms import *
from gerenciaAula.models import Usuario
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

    ROLE_CHOICE = (
        ('1', 'Direção'),
        ('2', 'Coordenação'),
        ('3', 'Docente'),
    )

    BOOLEAN_CHOICES = (
        (True, 'Sim'),
        (False, 'Não')
    )

    SUBJECTS = (
        ('mat', 'Matemática'),
        ('por', 'Português'),
        ('his', 'História')
    )

    CLASSES = (
        ('1', '1° Ano'),
        ('2', '2° Ano'),
        ('3', '3° Ano')
    )

    nome = forms.TextInput()
    eventual_doc = forms.ChoiceField(
        label='Professor Eventual',
        choices=BOOLEAN_CHOICES,
        initial=1,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    nivel_usuario = forms.ChoiceField(
        # label='Cargo',
        choices=ROLE_CHOICE,
        initial=2,
        # # coerce=str,
        # widget=forms.Select
    )

    class Meta:
        model = Usuario
        fields = ('nome', ) #'nivel_usuario',) #, 'nivel_usuario', 'eventual_doc', 'cod_turma', 'cod_disc')
    
    # is_temporary_teacher = forms.ChoiceField(
    #     label='Professor Eventual',
    #     choices=BOOLEAN_CHOICES,
    #     widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    # )

    # nome = forms.TextInput()
    # role = forms.ChoiceField(
    #     # label='Cargo',
    #     choices=ROLE_CHOICE,
    #     # coerce=str,
    #     widget=forms.Select
    # )
    # teached_subject = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=SUBJECTS
    # )
    # teached_classes = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=CLASSES
    # )
    
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print('pass1: ', password1, ' | pass2: ', password2)
        if password1 and password2 and password1 != password2:
            print("Deu erro na senha")
            raise forms.ValidationError('Passwords do not match.')
        print("AS senhas estão iguais")
        return password2

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #     return user

class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    }