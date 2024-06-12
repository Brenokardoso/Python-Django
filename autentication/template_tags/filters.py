from django import template


register = template.Library()


@register.filter(name="filter_one")
def teste_value(value):
    return f"O valor de value é de : {value}"
