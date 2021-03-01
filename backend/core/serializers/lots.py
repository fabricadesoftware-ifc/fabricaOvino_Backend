from rest_framework import serializers 
from backend.core.models import Lots

class LotsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Lots
        fields = ["id", "sheep", "user", "date","name"]

class LotsDetailSerializer(serializers.ModelSerializer):
    sheep = serializers.CharField(source="sheep.earringNumber", read_only=True)
    user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Lots
        fields = ["id", "sheep", "user", "date","name"]