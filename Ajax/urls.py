from django.urls import path, re_path
from .views import ajax_function, home, search
from django.conf.urls import url, include


urlpatterns = [
    path('ajax/', ajax_function, name='ajax_url'),
    path('search/', search, name='search_url'),
    path('', home, name='home_url'),
]


