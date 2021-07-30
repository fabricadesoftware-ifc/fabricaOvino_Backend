from rest_framework import status, viewsets
from rest_framework.response import Response
from backend.core.models import Sheep, Weight
from backend.core.serializers import WeightSerializer


class WeightViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

    def create(self, request):
        sheep = Sheep.objects.get(id=request.data["sheep"])
        serializer = WeightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
