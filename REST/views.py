from django.contrib.auth.models import User
from base.models import Contact
from .serializers import UserSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action


#Для доступа и авторизации
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


#Представление которое описывает наш API
class ContactViewSet(viewsets.ModelViewSet):
    #lookup_field = "pk"
    queryset = Contact.objects.all() #.order_by('phone')
    serializer_class = ContactSerializer
    #permission_classes = (IsAdminUser,)


# Представление которое описывает наш API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (AllowAny,)
    #lookup_field = "pk"

    def get_queryset(self):
        return User.objects.order_by("-pk")
