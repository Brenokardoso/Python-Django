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
    id = request.POST.get("id")
    print(f"Valor do ID {id}")
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    number_id = request.POST.get("numero_id")
    nome_cargo = request.POST.get("cargo_name")
    lotacao = request.POST.get("lotacao")
    cargo = Cargos(number_id, nome_cargo, lotacao)
    cargo_2 = Cargos.objects.get(id=7)
    # cargo.save() //manyTomany -> add or set()

    dados = {
        "nome": nome,
        "email": email,
        "senha": senha,
    }
    pessoa = Pessoa(
        id=id,
        nome=nome,
        email=email,
        senha=senha,
    )
    pessoa.save()
    cargo.save()
    pessoa.cargo.add(cargo)
    return render(request, "cadastro.html", {"dados": dados})


def valida_formulario(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    return HttpResponse(json.dumps({"nome": nome, "email": email}))


def listagem(request):
    pessoas = Pessoa.objects.all()
    pessoa = Pessoa.objects.get(nome="Breno")
    cargo1 = Cargos.objects.get(id=1)
    cargo2 = Cargos.objects.get(id=2)
    pessoa.cargo.add(cargo1, cargo2)
    filtro = Pessoa.objects.filter(cargo=cargo1)
    all_jobs = pessoa.cargo.all()
    print(f"filtro = {filtro}")
    print(f"{all_jobs}")
    pessoa.save()
    return render(request, "listagem.html", {"pessoas": pessoas})


def listar_unico(request, number_page):
    pessoa = Pessoa.objects.get(id=number_page)
    return render(request, "listar_unico.html", {"pessoa": pessoa})
