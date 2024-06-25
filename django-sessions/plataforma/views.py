from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    # if request.session["logado"] == True:
    if request:
        return render(request, "home.html")
    else:
        return redirect("/auth/login/?status=5")
