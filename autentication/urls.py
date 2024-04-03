from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',view=views.home),
    path('cadastro/',views.cadastro),
]

# # Usando o explorador de arquivos e importações de forma direta
# urlpatterns = [
#     path('cadastro',cadastro)
# ]