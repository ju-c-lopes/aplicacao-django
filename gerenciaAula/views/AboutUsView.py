from django.shortcuts import render


def sobre_nos(request):
    return render(request, "about-us/about-us.html")
