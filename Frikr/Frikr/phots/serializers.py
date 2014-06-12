__author__ = 'koke07'
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from models import Photo


class UserSerializer(serializers.Serializer):
    id = serializers.Field() #Campo lectura
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def restore_object(self, attrs, instance=None):

        if not instance:
            instance = User()

        instance.first_name = attrs.get('first_name')
        instance.last_name = attrs.get('last_name')
        instance.username = attrs.get('username')
        instance.email = attrs.get('email')
        new_password = make_password(attrs.get('password'))
        instance.password= new_password

        return instance

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Photo

