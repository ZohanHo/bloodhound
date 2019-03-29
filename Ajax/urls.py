from django.urls import path, include
from .views import ajax_function, home, search

urlpatterns = [
    path('ajax/', ajax_function, name='ajax_url'),
    path('search/', search, name='search_url'),
    path('', home, name='home_url'),
]


