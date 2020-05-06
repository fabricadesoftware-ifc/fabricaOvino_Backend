from rest_framework import serializers

from backend.core.models import Birth


class BirthSerializer(serializers.ModelSerializer):
    sheep = serializers.CharField(source="sheep.earringNumber", read_only=True)
    user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Birth
        fields = ["id", "sheep", "user", "date", "newborns_quantity"]
