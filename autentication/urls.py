from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',view=views.home),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('valida_formulario/',views.valida_formulario,name='valida_formulario'),
    path('listagem/',views.listagem,name="listagem")
]
