
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from .settings import DEBUG, MEDIA_ROOT , MEDIA_URL
from mainpage.views import show_mainpage
from django.conf.urls.static import static
from feedback.views import show_feedback , show_confirmed
from cart.views import show_cart
from catalog.views import show_catalog, show_product
from auntification.views import show_registration, show_login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_mainpage),
    path('catalogue/', show_catalog, name='filter_products'),
    path('feedback/', show_feedback, name='feedback_view'),
    path('confirmed/', show_confirmed),
    path('cart/', show_cart),
    path('registration/', show_registration),
    path('login/', show_login),
    path('product/<product_pk>', show_product, name='product')
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
