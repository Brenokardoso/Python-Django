from django.contrib import admin
from .models import Pessoa, Cargos, Pedido


# admin.site.register(Pessoa) // Registrando no modulo de admin o Modelo de Pessoa
# admin.site.register(Cargos) // Registrando no módulo de admin o Modelo de Cargos


class PedidoInLine(admin.TabularInline):
    model = Pedido
    list_display = ["nome", "quantidade", "descricao"]
    can_delete = True
    max_num = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ["foto", "complete_name", "email"]
    readonly_fields = ["senha"]
    search_fields = ["nome"]
    list_filter = ["cargo"]
    inlines = [PedidoInLine]


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = ["nome"]
