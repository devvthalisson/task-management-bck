from rest_framework import serializers
from .models import Task
from apps.users.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'completed',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'id': { 'read_only': True },
            'onwer': { 'read_only': True },
            'created_at': { 'read_only': True },
        }