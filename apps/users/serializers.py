from typing import Dict, Any
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': { 'write_only': True }
        }

    def create(self, validation_data:Dict[str, Any]) -> User:
        user = User.objects.create_user(**validation_data)
        return user