from rest_framework import viewsets

from backend.core.models import Sheep
from backend.core.serializers import SheepSerializer


class SheepViewSet(viewsets.ModelViewSet):
    queryset = Sheep.objects.all()
    serializer_class = SheepSerializer
