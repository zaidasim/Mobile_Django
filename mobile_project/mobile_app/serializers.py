from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Model:
        model=Item
        fields = '__all__'