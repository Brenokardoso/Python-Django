from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('auth/',include('autentication.urls')),
]
