from rest_framework import serializers
from backend.core.models import Weight


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ["id", "sheep", "user", "date", "observations", "weight"]


class WeightDetailSerializer(serializers.ModelSerializer):
    sheep = serializers.CharField(source="sheep.earringNumber", read_only=True)
    user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Weight
        fields = ["id", "sheep", "user", "date", "observations", "weight"]
