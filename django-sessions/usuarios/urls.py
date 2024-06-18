from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("", home),
    path("login/", login, name="login"),
    path("cadastro/", cadastro, name="cadastro"),
    path("pessoas/", pessoas, name="pessoas"),
]
