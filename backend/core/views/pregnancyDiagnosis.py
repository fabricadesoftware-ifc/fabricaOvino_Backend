from rest_framework import status, viewsets
from rest_framework.response import Response

from backend.core.models import PregnancyDiagnosis, Sheep
from backend.core.serializers import PregnancyDiagnosisSerializer


class PregnancyDiagnosisViewSet(viewsets.ModelViewSet):
    lookup_field = "id"

    queryset = PregnancyDiagnosis.objects.all()
    serializer_class = PregnancyDiagnosisSerializer

    def create(self, request):
        sheep = Sheep.objects.get(id=request.data["sheep"])
        serializer = PregnancyDiagnosisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if request.data["diagnosis"]:
            sheep.pregnant = True
            sheep.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
