from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("shop", views.shop, name='shop'),
    path("players", views.players, name='players'),
    path("about", views.about, name='about')
    
]