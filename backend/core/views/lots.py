from backend.core.models import Lots
from backend.core.serializers import LotsSerializer
from rest_framework import viewsets


class LotsViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Lots.objects.all()
    serializer_class = LotsSerializer
