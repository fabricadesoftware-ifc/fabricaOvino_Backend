from rest_framework import status, viewsets
from rest_framework.response import Response
from backend.core.models import Lots, Sheep
from backend.core.serializers import LotsSerializer


class LotsViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Lots.objects.all()
    serializer_class = LotsSerializer

    def create(self, request):
        sheep = Sheep.objects.get(id=request.data["sheep"])
        serializer = LotsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)