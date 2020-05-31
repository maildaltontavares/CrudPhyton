
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('contato/', views.contato,name='contato'),
    path('usuario/', views.usuario,name='usuario'),
    path('year/<int:year>', views.novidade_anual, name='novidade'),
    path('registro/', views.registro, name='add'),
    path('addUser/', views.addUser, name='addUser'),
    path('altUser/<int:id>', views.altUser, name='altUser'),
    path('excUser/<int:id>', views.excUser, name='excUser'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('home/',views.home,name='home'),



]