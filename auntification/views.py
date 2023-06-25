from django.shortcuts import render,redirect 
from .models import User
from catalog.models import Product
from django.db.utils import IntegrityError


# Create your views here.
def show_registration(request):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
    context={
        'login':login
    }
    response  = render(request, "auntificationapp/reg.html",context={'login':login})
    if request.method == "GET" and request.COOKIES.get('LogIn') is not None:
        return redirect('../')
    if request.method == "POST":
        if request.POST.get('name') == 'search':
            search_req = request.POST.get('searched-product')
            list_searched = Product.objects.filter(name__contains=search_req)
            if len(list_searched) < 1:
                nothing = f"We doesn't have product named {search_req}"
                respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'nothing':nothing,'login':login})
                return respose
            respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'login':login})
            return respose
        else:
            name=request.POST.get('name')
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            users = User.objects.all()
            for user in users:
                if password == password_confirm:
                    if name != user.name:
                        if email != user.email:
                            if phone != user.phone:
                                UserNew = User(name=request.POST.get('name'),password=request.POST.get('password'),phone=request.POST.get('phone'),email=request.POST.get('email'))
                                UserNew.save()
                                response  = render(request, "auntificationapp/reg.html",context={'login':login})
                                response.set_cookie('LogIn', True)
                                return response
                            else:
                                context['error_text']= 'Phone number is already taken'
                                print("phone")
                                response  = render(request, "auntificationapp/reg.html", context)
                                return response
                        else:
                            context['error_text']= 'Email is already taken'
                            print("email")
                            response  = render(request, "auntificationapp/reg.html", context)
                            return response
                    else:
                        context['error_text']= 'Nickname is already taken'
                        print("name")
                        response  = render(request, "auntificationapp/reg.html", context)
                        return response
                else:
                    context['error_text']= 'Паролі не співпадають!'
                    response  = render(request, "auntificationapp/reg.html", context)
                    return response

    return response 

def show_login(request):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
    context={
        'login':login
    }
    response = render(request, "auntificationapp/login.html",context={'login':login})
    if request.method == 'GET' and request.COOKIES.get('LogIn') is not None:
        return redirect('../')
    if request.method == "POST":
        if request.POST.get('name') == None:
            search_req = request.POST.get('searched-product')
            list_searched = Product.objects.filter(name__contains=search_req)
            if len(list_searched) < 1:
                nothing = f"We doesn't have product named {search_req}"
                respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'nothing':nothing,'login':login})
                return respose
            respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'login':login})
            return respose
        else:
            name = request.POST.get("name")
            password = request.POST.get("password")
            users = User.objects.all()
            for user in users:
                if password == user.password and name == user.name:
                    response.set_cookie('LogIn', True)
                    return response
            else:
                for user in users:
                    if name != user.name:
                        print('password')
                        response = render(request, "auntificationapp/login.html", context={'error_text' : 'You enter wrong nickname'})
                        return response
                    else:
                        if name == user.name and password != user.password:
                            print('name')
                            context['error_text']= 'You entered wrong password'
                            response  = render(request, "auntificationapp/login.html", context)
                            return response
    return response