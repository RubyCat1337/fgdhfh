from django import template

register = template.Library()

@register.simple_tag 
def count_products_in_cart(request):
    products_in_cart = request.COOKIES.get('product') 
    if products_in_cart == None:
        pass
    else:
        
        products_in_cart = products_in_cart.split(' ')
        products_count = len(products_in_cart)
        return products_count