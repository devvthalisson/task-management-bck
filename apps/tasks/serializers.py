from rest_framework import serializers
from .models import Task
from apps.users.models import User


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

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