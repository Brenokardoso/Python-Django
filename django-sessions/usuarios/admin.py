from django.contrib import admin
from .models import *

# admin.site.register(Usuario) // Método padrão de registros

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome","email"]
    readonly_fields = ["senha"]
    