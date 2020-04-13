from rest_framework import serializers

from backend.core.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ["id", "name"]
