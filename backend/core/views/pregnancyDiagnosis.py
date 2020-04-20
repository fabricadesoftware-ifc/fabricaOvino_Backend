from rest_framework import viewsets

from backend.core.models import PregnancyDiagnosis
from backend.core.serializers import PregnancyDiagnosisSerializer


class PregnancyDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = PregnancyDiagnosis.objects.all()
    serializer_class = PregnancyDiagnosisSerializer
