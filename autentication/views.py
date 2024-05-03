from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):
    return HttpResponse(content=F"Home Page Base Auth Controller")

def cadastro(request):
    # O envio de parametros é sempre via dicionário nas views 
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        dados = {'nome' : nome,'email' : email}
        return render(request,'cadastro.html',{'dados':dados})
    
    elif request.method == "GET":
        nome = request.GET.get("nome")
        email = request.GET.get("email")
        return HttpResponse(json.dumps({'nome': nome,'email': email}))

def valida_formulario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    return HttpResponse(json.dumps({'nome': nome,'email': email}))




# def cadastro(request):
#     nome = "Breno"
#     idade = 22
#     profissao = 'garoto de programa'
#     atributos_cadastro = [{
#         "nome" : nome,
#         "idade" : idade,
#         "profissao" : profissao,
#     },{
#         "nome" : "Lucas",
#         "idade" : "23",
#         "profissao" : "Vendedor",
#     },
#     {
#         "validator" : True
#     }]
#     lista_de_compras = ["abacaxi","pera","maça"]

#     # Para renderizar os valores no HTML você faz assim:
#     # atributos_cadastro.nome da variavel -> CERTO
#     # atributos_cadastro[nome da variavel] -> ERRADO

#     return render(request,"cadastro.html",{"atributos_cadastro":atributos_cadastro,
#                                             "compras" : lista_de_compras})