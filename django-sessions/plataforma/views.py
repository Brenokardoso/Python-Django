from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages as msg


@login_required(login_url="/auth/login/")
def home(request):
    if request:
        return render(request, "home.html")
    else:
        msg.add_message(
            request,
            constants.WARNING,
            "Você não está logado no sistema" "\n" "faça login",
        )
        return redirect("/auth/login/")
