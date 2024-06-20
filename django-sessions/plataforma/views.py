from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.session["logado"] == True:
        return HttpResponse("Você está no sistema!")
    else:
        return redirect("/auth/login/?status=5")
