from django.http import HttpResponse
from django.shortcuts import render


def home(request, nome):
    return render(request, 'hello.html', {'nome': nome})

