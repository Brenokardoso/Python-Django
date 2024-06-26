from django.contrib import admin
from autentication.models import Pessoa, Cargos, Pedido
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse
from django.shortcuts import render

# admin.site.register(Pessoa) // Registrando no modulo de admin o Modelo de Pessoa
# admin.site.register(Cargos) // Registrando no módulo de admin o Modelo de Cargos


class PedidoInLine(admin.TabularInline):
    model = Pedido
    list_display = ["nome", "quantidade", "descricao"]
    can_delete = True
    max_num = 1


@admin.register(Pessoa)
class PessoaAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ["get_image", "complete_name", "email"]
    readonly_fields = ["senha"]
    search_fields = ["nome"]
    list_filter = ["cargo"]
    inlines = [PedidoInLine]

    def mostra_pessoa(self, request, pessoa):
        return HttpResponse(f"tome a request")

    def lista_pessoa(self, request, people):
        pessoa = Pessoa.objects.filter(nome=people.nome)
        print(f"valor do params pessoa : {people}")
        return render(request, "listagem.html", context={"pessoas": pessoa})

    lista_pessoa.label = "Lista"
    mostra_pessoa.label = "mostrar pessoa"

    change_actions = ("mostra_pessoa", "lista_pessoa")


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = ["nome"]
