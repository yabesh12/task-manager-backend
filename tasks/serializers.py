from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model excluding the 'owner' field."""
    class Meta:
        model = Task
        exclude = ['owner']
