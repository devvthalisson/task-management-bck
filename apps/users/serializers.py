from typing import Dict, Any
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password as django_validate_password
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError


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
    
    def validate_password(self, value: User) -> User:
        if value:
            try:
                django_validate_password(value)
            except DjangoValidationError as e:
                raise ValidationError(e.messages)
            
            return value
        
        raise ValidationError('Password is required')