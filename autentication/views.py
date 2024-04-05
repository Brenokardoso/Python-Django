from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = "Breno"
    idade = 22
    profissao = 'garoto de programa'
    atributos_cadastro = [{
        "nome" : nome,
        "idade" : idade,
        "profissao" : profissao,
    },{
        "nome" : "Lucas",
        "idade" : "23",
        "profissao" : "Vendedor",
    }]

    # Para renderizar os valores no HTML você faz assim:
    # atributos_cadastro.nome da variavel -> CERTO
    # atributos_cadastro[nome da variavel] -> ERRADO
    return render(request,"cadastro.html",{"atributos_cadastro":atributos_cadastro})

def home(request):
    return HttpResponse(content=F"Home Page Base Auth Controller")
