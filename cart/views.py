from django.shortcuts import render
from catalog.models import Product
from onlainshop.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_CHAT_ID
import cart.telegram as tele
from django.core import serializers
from django.http import JsonResponse
# Create your views here.



def show_cart(request):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
    if request.COOKIES.get('product') is not None:
        products_pk = request.COOKIES['product'].split(' ')
        list_products = list()
        for product in products_pk:
            list_products.append(Product.objects.get(pk=product))
        response = render(request, 'cartapp/cart.html', {'products': list_products,'login':login})
    else:
        list_products = list()
        response = render(request, 'cartapp/cart.html', {'products': list_products,'empty':'true','login':login})

    if request.method == 'POST':
        if request.POST.get('name') == 'search':
            search_req = request.POST.get('searched-product')
            list_searched = Product.objects.filter(name__contains=search_req)
            if len(list_searched) < 1:
                nothing = f"We doesn't have product named {search_req}"
                respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'nothing':nothing,'login':login})
                return respose
            respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'login':login})
            return respose
        if request.POST.get('name') == 'buy':
            product_readed = []
            name = request.POST.get('UserName')
            email = request.POST.get('email')
            print(name,email)
            price = 0
            message = f'Order \nName: {name} \nEmail: {email}\nProduct:'
            for product in list_products:
                if product in product_readed:
                    continue
                    
                else:

                    count = list_products.count(product)
                    price += product.price * count
                    message += f'\n{product.name},Items: {count}, Price:{int(product.price)*count}$'
                    product_readed.append(product)
            message += f'\nFinal price - {price}$'
            tele.bot_send(TELEGRAM_BOT_TOKEN,TELEGRAM_BOT_CHAT_ID,message)
            print(message) 
            response.delete_cookie('product')
            return response
        else:
            pk_deleted = request.POST.get('product_pk_deleted')
            print(pk_deleted)

            if pk_deleted:
                print(products_pk)
                products_pk.remove(pk_deleted)
                print(products_pk)
                products_pk = ' '.join(products_pk)
                print(products_pk)
                if products_pk:
                    list_products = list()
                    # for product in products_pk.split(" "):
                    #     list_products.update({"product" : Product.objects.filter(pk=product)})
                    list_products = Product.objects.filter(pk__in=products_pk.split(" ")).values()
                    print(list_products)
                    list_products = list(list_products)
                    response = JsonResponse({'list_products': list_products})
                    response.set_cookie('product', products_pk)
                    return response
                else:
                    response = render(request, 'cartapp/cart.html', {'products': [],'empty':'true','login':login})
                    response.delete_cookie('product')
                    
                    return response
    return response
