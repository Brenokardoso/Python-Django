from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect, render
from hashlib import sha256
from django.contrib import messages as msg
from django.contrib.messages import constants


def home(request):
    return HttpResponse("Auth Page")


def login(request):
    return render(request, "login.html")


def cadastro(request):
    return render(request, "cadastro.html")


def pessoas(request):

    if request.session["logado"] == False:
        msg.add_message(
            request, constants.WARNING, "Usuário não conectado ao sistema,faça o login"
        )
        return redirect("/auth/login/")
    else:
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
        msg.add_message(
            request,
            constants.ERROR,
            "Campos de nome e/ou email e/ou senha vazios,preencha-os!",
        )
        return redirect("/auth/cadastro/")

    if len(Usuario.objects.filter(nome=nome).filter(email=email)) > 0:
        msg.add_message(
            request,
            constants.ERROR,
            "Este nome de usuario e email já estão cadastrados",
        )
        return redirect("/auth/cadastro/")

    senha = sha256(senha.encode()).hexdigest()

    user = Usuario(nome=nome, email=email, senha=senha)
    user.save()

    msg.add_message(request, constants.SUCCESS, "Usuário cadastrado com sucesso!")
    return redirect("/auth/cadastro/")


def validate_login(request):

    try:
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        print(f"O Email {email} senha {senha}")

    except:
        print("Não foi posível capturar os valores")

    if (senha == None or senha == "") or (senha == None or senha == ""):
        msg.add_message(
            request,
            constants.WARNING,
            "Email ou senha inválidos,preencha os campos corretamente",
        )
        return redirect("/auth/login/")

    elif len(senha) < 8:
        msg.add_message(
            request,
            constants.WARNING,
            "Número de caracteres da senha precisa ser maior",
        )
        return redirect("/auth/login/")

    elif len(Usuario.objects.filter(email=email)) == 0:
        msg.add_message(request, constants.WARNING, "Usuário não cadastrado")
        return redirect("/auth/login/")

    else:
        request.session["logado"] = True
        request.session["user_id"] = True
        msg.add_message(request, constants.SUCCESS, "Redirecionado com sucesso")
        return redirect("/plataforma/home/")


def sair(request):
    try:
        request.session.flush()
        return redirect("/auth/login/")

    except KeyError:
        msg.add_message(request, constants.WARNING, "Chave de Id não existe")
        return redirect("/auth/login/")


# def sair(request):j
# time_min = request.session.get_expiry_age() / 60  # minutos
# time_hrs = time_min / 60  # horas
# time_day = time_hrs / 24
# expiry_days = request.session.get_expiry_date()
# return HttpResponse(
#     f"O tempo para o usuário expirar é de {time_day} dias ou {time_hrs} horas ou {time_min} minutos"
# )
# request.session["logado"] = False
# request.session["user_id"] = False
# request.session.clear() # Apaga todos os valores armazenados nesta chave
# request.session.flush()  # Apaga tudo,até a chave
# return redirect("/auth/login/")
