from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def logout_user(request):
    logout(request)
    return redirect("/")
