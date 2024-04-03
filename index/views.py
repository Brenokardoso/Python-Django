from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(content="Bem vindo a sua Home")
