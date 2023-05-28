from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="home"),
    path('signup/',sign_up, name="signup"),
    path('product/',product),
    path('book/',book),
    path('login/',login, name="login"),

]
