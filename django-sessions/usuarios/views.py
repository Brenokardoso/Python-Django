from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from hashlib import sha256
from django.contrib import messages as msg
from django.contrib.messages import constants
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login as authLogin, logout
from django.contrib.auth.decorators import login_required
from .models import EnderecoUsuario


def home(request):
    return HttpResponse("Auth Page")


def login(request):
    if request.user.is_authenticated:
        return redirect("/plataforma/home")
    else:
        return render(request, "login.html")


def cadastro(request):
    return render(request, "cadastro.html")


@login_required(login_url="/auth/login/")
def pessoas(request):

    people = AuthUser.objects.all()
    return render(request, "pessoas.html", {"pessoas": people})


def validate_cadastro(request):

    try:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        rua = request.POST.get("rua")
        num_rua = request.POST.get("num_rua")
        cep = request.POST.get("cep")

        print(f"os valores de rua {rua} numero {num_rua} e cep {cep}")

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

    if AuthUser.objects.filter(email=email).exists():
        msg.add_message(
            request,
            constants.ERROR,
            "Este email já está cadastrado",
        )
        return redirect("/auth/cadastro/")

    if AuthUser.objects.filter(username=nome).exists():
        msg.add_message(
            request,
            constants.ERROR,
            "Este nome de usuario está cadastrado",
        )
        return redirect("/auth/cadastro/")

    usuario = AuthUser.objects.create_user(
        username=nome,
        email=email,
        password=senha,
    )

    usuario.save()

    end_user = EnderecoUsuario(rua=rua, numero=num_rua, cep=cep, usuario=usuario)
    end_user.save()

    msg.add_message(
        request,
        constants.SUCCESS,
        "Usuário cadastrado com sucesso!",
    )
    return redirect("/auth/cadastro/")


def validate_login(request):

    try:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

    except:
        msg.add_message(
            request,
            constants.INFO,
            "Não foi posível capturar os valores de nome e email",
        )
        redirect("/auth/login/")

    try:
        usuario = authenticate(
            request=request,
            username=nome,
            email=email,
            password=senha,
        )

        authLogin(request, usuario)

    except:
        msg.add_message(request, constants.WARNING, "Usuário não existe!")
        return redirect("/auth/login/")

    return redirect("/plataforma/home/")


def sair(request):

    try:
        logout(request)
        # request.session.flush()
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
