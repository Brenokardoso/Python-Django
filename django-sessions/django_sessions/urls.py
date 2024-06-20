from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import home

urlpatterns = [
    path("", lambda request: redirect("auth/login")),
    path("admin/", admin.site.urls),
    path("auth/", include("usuarios.urls")),
    path("plataforma/", include("plataforma.urls")),
]
