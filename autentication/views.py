from django.shortcuts import render
from django.http import HttpResponse
import json
from django.db.models import Q
from .models import Pessoa, Cargos


def home(request):
    return HttpResponse(content=f"Home Page Base Auth Controller")


def cadastro(request):
    # O envio de parametros é sempre via dicionário nas views
    print(request)
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    number_id = request.POST.get("numero_id")
    nome_cargo = request.POST.get("cargo_name")
    lotacao = request.POST.get("lotacao")
    cargo = Cargos(number_id, nome_cargo, lotacao)
    cargo_2 = Cargos.objects.get(id=7)
    cargo.save()

    dados = {
        "nome": nome,
        "email": email,
        "senha": senha,
    }
    pessoa = Pessoa(
        nome=nome,
        email=email,
        senha=senha,
        cargo=cargo,
    )
    pessoa.save()
    return render(request, "cadastro.html", {"dados": dados})


def valida_formulario(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    return HttpResponse(json.dumps({"nome": nome, "email": email}))


def listagem(request):
    # Pessoa.objects.filter()
    pessoas = Pessoa.objects.all()
    cargo = Cargos.objects.get(id=2)
    new_job = pessoas.get(nome="Breno")
    new_job.cargo = cargo
    new_job.save()

    # pessoas = pessoas.exclude(nome__icontains="teste")

    return render(request, "listagem.html", {"pessoas": pessoas})


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
