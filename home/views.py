from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def home(request):
    return render(request, 'home.html')


# Faz o logout do usuário e direciona para home
def user_logout(request):
    logout(request)
    return redirect('home')
