from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls import  include, url

urlpatterns =[
    #url('$', views.home , name='home'),
    path('scrapy/', views.home , name="home"),
] 
