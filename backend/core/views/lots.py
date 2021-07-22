from backend.core.models import Lots
from backend.core.serializers import LotsSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response



class LotsViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Lots.objects.all()
    serializer_class = LotsSerializer

    def create(self, request):
        serializer = LotsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
