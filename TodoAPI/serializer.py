from rest_framework import serializers
from .models import Todoitem
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ['id', 'title', 'body', 'completed', 'created_at', 'updated_at']