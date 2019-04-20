from django.shortcuts import render
from rest_framework import status, viewsets
from languages.models import language
from .serializers import languageSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = languageSerializer

