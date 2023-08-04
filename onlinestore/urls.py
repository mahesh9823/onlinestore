"""
URL configuration for onlinestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from categories.views import CategoryView
from sellers.views import SellerView, SellerSignUp, SellerSignIn
from buyers.views import BuyerView, BuyerSignUp, BuyerSignIn
from products.views import ProductView
from cart.views import CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories', CategoryView, name="Categories"),
    path('buyers', BuyerView, name="Buyers"),
    path('buyerSignUp', BuyerSignUp, name="BuyerSignUp"),
    path('buyerSignIn', BuyerSignIn, name="BuyerSignIn"),
    path('sellers', SellerView, name="Sellers"),
    path('sellerSignUp', SellerSignUp, name="SellerSignUp"),
    path('sellerSignIn', SellerSignIn, name="SellerSignIn"),
    path('products', ProductView, name="Products"),
    path('cart', CartView, name="Cart")
]
