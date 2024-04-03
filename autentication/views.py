from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse(content = F"Faça o seu cadastro para prosseguir : {request}")

def home(request):
    return HttpResponse(content=F"Home Page Base Auth Controller")
