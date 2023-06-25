from django.shortcuts import render, redirect
from django.core.mail import send_mail
from catalog.models import Product
from django.views.decorators.csrf import csrf_exempt
from onlainshop.settings import EMAIL_HOST_USER
from .models import SendMail
# Create your views here.
def show_feedback(request):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
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
            name = request.POST.get('name')
            email = request.POST.get('email')
            order = request.POST.get('order')




            message_for_client = f"Vitaemo, {name}!\nThanks for the Review about the store:{order}"
            message_for_admin = f"Feedback from the client: {name}\nCustomer email: {email}\ncustomer feedback: {order}"

            check_email_user = send_mail(
                subject = "Онлайн магазин",
                message = message_for_client,
                from_email = EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently=False
            )

            check_email_admin = send_mail(
                subject = "Онлайн магазин",
                message = message_for_admin,
                from_email = EMAIL_HOST_USER,
                recipient_list = [EMAIL_HOST_USER],
                fail_silently=False
            )

            if check_email_admin and check_email_user:  
                SendMail.objects.create(name = name,email=email,order=order)
                return redirect('../confirmed/')
    return render(request, 'feedbackapp/feedback.html',context={'login':login})

def show_confirmed(request):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
    if request.method == 'POST':
        search_req = request.POST.get('searched-product')
        list_searched = Product.objects.filter(name__contains=search_req)
        if len(list_searched) < 1:
            nothing = f"We doesn't have product named {search_req}"
            respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'nothing':nothing,'login':login})
            return respose
        respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'login':login})
        return respose
    respose = render(request, "feedbackapp/confirmed.html",context={'login':login})
    return respose
    