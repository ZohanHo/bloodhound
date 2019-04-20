from django.contrib.auth.models import User
from languages.models import language
from rest_framework import serializers

# Serializers определяет представление API (кодировка данных на другой язык, чаще всего в JSON, реже в XML)
class languageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = language
        fields = ('id', 'url', 'name', 'paradigm')
