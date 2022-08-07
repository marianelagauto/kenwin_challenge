"""authentication views"""
# from django import forms
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@csrf_protect
def login_user(request):
    """user authentication"""
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request=request, user=user)
            return redirect('home')
        messages.error(request,'Usuario o contraseña incorrecta')
        return redirect('login')
    return render(request, 'login.html', {})


def logout_user(request):
    """cerrar sesion"""
    logout(request)
    return redirect('login')


@login_required
def home(request):
    """ home """
    return render(request, 'home.html', {})
    