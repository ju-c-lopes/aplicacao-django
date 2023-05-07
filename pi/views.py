from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'pagina-modelo.html') # A modificar string de retorno 