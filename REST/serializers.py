from django.contrib.auth.models import User
from base.models import Contact
from rest_framework import serializers




# Serializers определяет представление API (кодировка данных на другой язык, чаще всего JSON, XML)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers определяет представление API (кодировка данных на другой язык, чаще всего JSO, XML)
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ( 'user_id', 'id', 'name', 'phone', 'slug', 'url', "user")

# Serializers определяет представление API (кодировка данных на другой язык, чаще всего JSO, XML)
class ContactCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone', "slug")