from django import template

register = template.Library()

@register.simple_tag
def multiply(value, arg):
    return int(value) * int(arg)

@register.filter
def thousands(value):
    return f"{int(value):,}".replace(",", ".")

