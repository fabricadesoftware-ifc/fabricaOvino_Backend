from rest_framework import serializers
from backend.core.models import Shearing

class ShearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shearing
        fields = ["id", "sheep", "user", "date", "amountOfWool"]

class ShearingDetailSerializer(serializers.ModelSerializer):
    sheep = serializers.CharField(source="sheep.earringNumber", read_only=True)
    user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Shearing
        fields = ["id", "sheep", "user", "date","amountOfWool"]
