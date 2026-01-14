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
        read_only_fields = [
            'id', 'owner', 'created_at', 'updated_at'
        ]


class TaskChangeStatusSerializer(serializers.ModelSerializer):
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
        read_only_fields = [
            'id', 'owner', 'title', 'description', 'created_at', 'updated_at'
        ]

    def update(self, instance, validated_data):
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance


