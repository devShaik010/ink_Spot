
from django import template

register = template.Library()

@register.filter(name="multiply")
def multiply(n1,n2):
    return n1 * n2