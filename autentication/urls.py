from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',view=views.home),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('valida_formulario/',views.valida_formulario,name='valida_formulario'),
    path('lista/',views.listagem,name="lista"),
    path('listar_unico/<int:number_page>',views.listar_unico,name="listar_unico")
]
