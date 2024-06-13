from django.contrib import admin
from .models import Pessoa, Cargos


# admin.site.register(Pessoa) // Registrando no modulo de admin o Modelo de Pessoa
# admin.site.register(Cargos) // Registrando no módulo de admin o Modelo de Cargos


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ["nome", "email", "senha"]
    readonly_fields = ["senha"]
    search_fields = ["nome"]
    list_filter = ["cargo"]
    list_editable = ["email"]


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = ["nome"]
