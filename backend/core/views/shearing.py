from rest_framework import status, viewsets
from rest_framework.response import Response
from backend.core.models import Shearing, Sheep
from backend.core.serializers import ShearingSerializer

class ShearingViewSet(viewsets.ModelViewSet):
    lookup_field = "id" 
    queryset = Shearing.objects.all()
    serializer_class = ShearingSerializer

    def create(self, request):
        sheep = Sheep.objects.get(id=request.data["sheep"])
        serializer = ShearingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
