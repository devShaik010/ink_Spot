from django import template

register = template.Library()
@register.filter(name='check_cart')
def check_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    # print(product.name , cart)
    return False;