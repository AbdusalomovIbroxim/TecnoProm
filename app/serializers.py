from rest_framework import serializers
from .models import App

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'title', 'description']
