from django import template

register = template.Library()

@register.filter
def round_filter(value):
    value += 0.01
    return round(value)