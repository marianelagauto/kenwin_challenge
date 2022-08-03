"""authentication views"""
# from django import forms
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages


@csrf_protect
def login_user(request):
    """user authentication"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request=request, user=user)
            return redirect('home')
        messages.success(request, "Error")
        return redirect('login')
    return render(request, 'login.html', {})


def home(request):
    """ home """
    return render(request, 'home.html', {})
    