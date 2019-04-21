from django.urls import path, include
from .import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'contact', views.ContactListApiView) #this endpoint
#
# urlpatterns = [
#     path('', include(router.urls))
# ]


urlpatterns = [
    path('contact/', views.ContactListApiView.as_view()),
    path('contact/<pk>/', views.DetailListApiView.as_view()),
    path('contact/<pk>/edit/', views.ContactUpdateApiView.as_view(), name = "update"),
    path('contact/<pk>/delete/', views.ContactDeleteApiView.as_view(), name = "delete"),
    path('contact/<pk>/create/', views.ContactCreateApiView.as_view(), name = "create")
]