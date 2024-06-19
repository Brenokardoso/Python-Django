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
    try:
        status = request.GET.get("status")
        print(f"Valor do status = {status}")
    except:
        print("Houve uma exceção")
    return render(request, "cadastro.html", {"status": status})


def pessoas(request):
    people = Usuario.objects.all()
    return render(request, "pessoas.html", {"pessoas": people})


def validate(request):
    try:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
    except:
        return redirect("/auth/cadastro?status=4")

    if (
        (nome == None or nome == "")
        or (email == None or email == "")
        or (senha == None or senha == "")
    ):
        return redirect("/auth/cadastro?status=1")

    senha = sha256(senha.encode()).hexdigest()

    user = Usuario(nome=nome, email=email, senha=senha)
    user.save()

    return redirect("/auth/cadastro?status=0")
