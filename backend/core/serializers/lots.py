from backend.core.models import Lots
from rest_framework import serializers


class LotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lots
        fields = ["id", "date", "name"]
