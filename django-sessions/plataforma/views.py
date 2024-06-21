from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    # if request.session["logado"] == True:
    if (request.session.get("logado") == True) and (request.session["user_id"] == True):
        return render(request, "home.html")
    else:
        return redirect("/auth/login/?status=5")
