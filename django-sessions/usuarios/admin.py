from django.contrib import admin
from .models import *

admin.site.register(EnderecoUsuario)


# @admin.register(EnderecoUsuario)
# class AdminEnderecoUsuario(admin.ModelAdmin):
# list_display = ["usuario", "rua", "numero", "cep"]
