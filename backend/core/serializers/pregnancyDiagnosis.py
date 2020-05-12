from rest_framework import serializers

from backend.core.models import PregnancyDiagnosis


class PregnancyDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnancyDiagnosis
        fields = ["id", "sheep", "user", "date", "diagnosis"]


class PregnancyDiagnosisDetailSerializer(serializers.ModelSerializer):
    sheep = serializers.CharField(source="sheep.earringNumber", read_only=True)
    user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = PregnancyDiagnosis
        fields = ["id", "sheep", "user", "date", "diagnosis"]
