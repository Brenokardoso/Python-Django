from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def home(request):
    return HttpResponse("Auth Page")


def login(request):
    print(f"tipo da request {request.method}")
    return render(request, "login.html")


def cadastro(request):
    print(f"tipo da request {request.method}")
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    senha = request.POST.get("senha")

    user = Usuario()
    user.nome = nome
    user.email = email
    user.senha = senha
    user.save()

    usuarios = {"nome": nome, "email": email, "senha": senha}
    return render(request, "cadastro.html", context={"usuarios": usuarios})
