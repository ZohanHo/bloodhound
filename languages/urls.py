from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'languages', views.LanguageView) #ето ендпоинт


urlpatterns = [
    path('', include(router.urls))
]
