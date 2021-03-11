from django.utils.translation import gettext_lazy as _

from backend.core.models import Sheep
from rest_framework import serializers


class SheepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "lots", "birthday", "sex", "teethQuantity", "lactating"]


class SheepCreateNewbornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = ["id", "earringNumber", "breed", "category", "lots", "birthday", "sex", "teethQuantity", "lactating"]


class SheepDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    breed = serializers.CharField(source="breed.name", read_only=True)
    lots = serializers.CharField(source="lots.name", read_only=True)
    # sex = _(serializers.CharField(source="get_sex_display", read_only=True))
    sex = serializers.SerializerMethodField()

    class Meta:
        model = Sheep
        fields = [
            "id",
            "earringNumber",
            "breed",
            "category",
            "lots",
            "births",
            "birthday",
            "sex",
            "teethQuantity",
            "pregnant",
            "lactating",
            "shearing",
        ]
        depth = 1

    def get_sex(self, obj):
        return _(obj.get_sex_display())
