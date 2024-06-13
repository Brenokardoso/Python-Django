from django import template



register = template.Library()
"""
A class for registering template tags and filters. Compiled filter and
template tag functions are stored in the filters and tags attributes.
The filter, simple_tag, and inclusion_tag methods provide a convenient
way to register callables as tags.
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
