from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("", home),
    path("login/", login, name="login"),
    path("cadastro/", cadastro, name="cadastro"),
    path("pessoas/", pessoas, name="pessoas"),
    path("validate_cadastro/", validate_cadastro, name="validate_cadastro"),
    path("validate_login",validate_login,name='validate_login')
]
