from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'home.html') # A modificar string de retorno


def cadastro(request):
    return render(request, 'cadastro.html')