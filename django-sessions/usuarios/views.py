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

    msg.add_message(
        request,
        constants.SUCCESS,
        "Você entrou na página com sucesso!\t",
    )
    
    # msg.add_message(
    #     request,
    #     constants.INFO,
    #     "Mensagem de infomação para o usuário final",
    # )

    try:
        status = request.GET.get("status")
        print(f"Valor do status no login {status}")
    except:
        print("Não foi possível capturar o valor do status code")
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
        if request.session["logado"] == False:
            return redirect("/auth/login/?status=5")
        else:
            try:
                status = request.GET.get("status")
                print(f"valor do status : {status}")
            except:
                print("Houve uma exceção ao capturar o status")

            people = Usuario.objects.all()
            return render(request, "pessoas.html", {"pessoas": people})
    except:
        return redirect("/auth/login/?status=5")


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

    elif len(senha) < 8:
        return redirect("/auth/login/?status=2")

    elif len(Usuario.objects.filter(email=email)) == 0:
        return redirect("/auth/login/?status=3")

    else:
        request.session["logado"] = True
        request.session["user_id"] = True
        return redirect("/plataforma/home/")


def sair(request):
    try:
        del request.session["logado"]
        del request.session["user_id"]
        return redirect("/auth/login/")
    except KeyError:
        return redirect("/auth/login/?status=7")


# def sair(request):
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
