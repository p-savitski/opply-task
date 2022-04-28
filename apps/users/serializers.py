from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    @transaction.atomic()
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return super(UserSerializer, self).create(validated_data)

