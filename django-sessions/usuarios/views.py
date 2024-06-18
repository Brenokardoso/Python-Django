from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def home(request):
    return HttpResponse("Auth Page")


def login(request):
    return render(request, "login.html")


def cadastro(request):
    return render(request, "cadastro.html")


def pessoas(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    print(f"nome {nome} email {email} e senha {senha}")

    if nome or email or senha is not None:
        user = Usuario()
        user.nome = nome
        user.email = email
        user.senha = senha
        user.save()

    else:
        print("O nome não foi salvo por falta de dados")
        pass

    pessoas = Usuario.objects.all()

    return render(request, "pessoas.html", {"pessoas": pessoas})
