from rest_framework import serializers

from backend.core.models import Sheep


class SheepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "birthday", "sex", "teethQuantity"]


class SheepCreateNewbornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "birthday", "sex", "weight"]


class SheepDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    breed = serializers.CharField(source="breed.name", read_only=True)
    sex = serializers.CharField(source="get_sex_display", read_only=True)

    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "birthday", "sex", "teethQuantity", "pregnant"]
