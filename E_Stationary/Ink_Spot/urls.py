from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="home"),
    path('signup/',sign_up, name="signup"),
    path('login/',login, name="login"),
    path('product/',product,name='product'),
    path('book/',book),
    path('cart/',cart, name="cart"),
    path('check-out/',check_out, name="check_out"),

]
