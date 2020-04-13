from rest_framework import serializers

from backend.core.models import Sheep


class SheepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "birthday", "sex", "teethQuantity", "mother", "father"]
