from django import template

register = template.Library()

@register.simple_tag
def multiply(value, arg):
    return int(value) * int(arg)
