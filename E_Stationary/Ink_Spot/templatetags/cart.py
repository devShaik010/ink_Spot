from django import template

register = template.Library()
@register.filter(name='check_cart')
def check_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;

@register.filter(name='check_count')
def check_count(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;