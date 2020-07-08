from rest_framework import viewsets

from backend.core.models import Breed
from backend.core.serializers import BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    pagination_class = None
