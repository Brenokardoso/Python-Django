from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = "Breno"
    idade = 22
    profissao = 'garoto de programa'
    atributos_cadastro = {
        "nome" : nome,
        "idade" : idade,
        "profissao" : profissao,
    }
    return render(request,"cadastro.html",{"nome":nome,"idade":idade,"profissao":profissao})

def home(request):
    return HttpResponse(content=F"Home Page Base Auth Controller")
