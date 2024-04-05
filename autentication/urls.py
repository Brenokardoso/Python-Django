from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',view=views.home),
    path('cadastro/',views.cadastro),
]
