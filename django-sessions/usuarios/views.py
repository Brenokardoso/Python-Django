from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def home(request):
    return HttpResponse("Auth Page")


def login(request):
    return render(request, "login.html")


def cadastro(request):
    # status = request.POST.get("status")
    # msg = request.POST.get("msg")
    # dict = {"status": status, "msg": msg}

    return render(request, "cadastro.html")


def pessoas(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    senha = request.POST.get("senha")

    # if len(nome.strip()) == 0 or len(email.strip()) == 0:
    #     return lambda redirect: redirect("auth/cadastro?status=1")

    # if len(senha) < 8:
    print(f"valores de nome {type(nome)} email{type(email)} senha {type(senha)}")
    if (nome == None or "") and (email == None or "") and (senha == None or ""):
        return lambda redirect: redirect("auth/cadastro?status=2")

    # usuario = Usuario.objects.filter(email=email)

    # if len(usuario) > 0:
    #     return lambda redirect: redirect("auth/cadastro?status=3")

    # senha = sha256(senha.encode()).hexdigest()

    # user = Usuario(nome=nome, email=email, senha=senha)
    # user.save()

    people = Usuario.objects.all()

    return render(request, "pessoas.html", {"pessoas": people})
