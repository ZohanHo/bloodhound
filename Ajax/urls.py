from django.urls import path, include
from .views import ajax_function, home

urlpatterns = [
    path('ajax/', ajax_function, name='ajax_url'),
    path('', home, name='home_url'),
]


