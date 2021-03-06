from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, ContactViewSet

# Роуты моего API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contact', ContactViewSet)



urlpatterns = [
    url(r'^api-v.1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]