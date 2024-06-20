from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("/plataforma/home")),
    path("home/", views.home, name="home"),
]
