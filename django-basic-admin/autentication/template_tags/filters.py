from django import template



register = template.Library()
"""
Uma classe para registrar tags e filtros de modelo. Filtro compilado e
As funções de tag de modelo são armazenadas nos atributos de filtros e tags.
Os métodos filter, simple_tag e inclusão_tag fornecem uma maneira conveniente
maneira de registrar callables como tags.
"""

@register.filter(name="filter_one")
def teste_value(value):
    return f"O valor de value é de : {value}"


@register.filter("replace")
def replace_name(string) -> str:
    return f"O novo valor é de {string}"


@register.filter("string_has_none")
def sustitute_none_name(obj_name):
    obj_name = "Informação Inexistente" if obj_name == None else obj_name
    return obj_name
