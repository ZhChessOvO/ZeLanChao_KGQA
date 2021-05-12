"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from medicine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('single/', views.single),
    path('login/', views.login),
    path('logout/', views.logout),
    path('passageindex/', views.passageindex),
    path('getpassage/', views.getpassage),
    path('searchresult/', views.searchresult),
    path('qs/', views.qs),
    path('submitsatisfaction/', views.submitsatisfaction),
    path('question/', views.question),
    path('sendemail/', views.sendemail),
    path('subscribe/', views.subscribe),
    path('register/', views.register),
    path('recommend/', views.recommend),
]
