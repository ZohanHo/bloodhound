"""bloodhound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import PopupView, Submit, Get_absolute_url_list, Get_absolute_url_detail

urlpatterns = [
    path('', PopupView, name="popup_url"),
    path('submit/', Submit, name="submit_url"),

    path('get_abs_url_list/', Get_absolute_url_list, name="get_abs_url_list"),
    path('get_abs_url_detail/<pk>/', Get_absolute_url_detail, name="get_abs_url_detail"),
]
