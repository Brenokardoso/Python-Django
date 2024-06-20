from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect,render
from hashlib import sha256


def home(request):
    return HttpResponse("Auth Page")


def login(request):

    status = request.GET.get("status")
    print(f"Valor do status no login {status}")
    try:
        email = request.POST.get("email")
        senha = request.POST.get("senha")
    except:
        print("Não foi possível caprtuar os dados")

    return render(request, "login.html", {"status": status})


def cadastro(request):

    try:
        status = request.GET.get("status")
        print(f"Valor do status = {status}")
    except:
        print("Houve uma exceção")
    return render(request, "cadastro.html", {"status": status})


def pessoas(request):

    try:
        status = request.GET.get("status")
        print(f"valor do status : {status}")
    except:
        print("Houve uma exceção ao capturar o status")

    people = Usuario.objects.all()
    return render(request, "pessoas.html", {"pessoas": people})


def validate_cadastro(request):

    try:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
    except:
        print("Não foram possível capturar os dados")

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


def validate_login(request):

    try:
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        print(f"O Email {email} senha {senha}")
    except:
        print("Não foi posível capturar os valores")

    if (senha == None or senha == "") or (senha == None or senha == ""):
        return redirect("/auth/login/?status=1")

    if len(senha) < 8:
        return redirect("/auth/login/?status=2")

    return redirect("/auth/pessoas/?status=0")
