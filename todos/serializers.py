from rest_framework import serializers

from .models import Todos

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'

        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': False},
            'due_date': {'required': False}
        }