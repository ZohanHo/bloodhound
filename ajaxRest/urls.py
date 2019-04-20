from django.urls import path, re_path
from django.conf.urls import url, include
from REST.views import UserViewSet, ContactViewSet
from .views import renderList, change



urlpatterns = [
    path('', renderList, name='renderList_url'),
    path('change/', change, name='change_for_post_url'),
    path('api/users/', UserViewSet.as_view({'get': 'list'})),
    path('api/contact/', ContactViewSet.as_view({'get': 'list'})),
]

