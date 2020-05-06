from rest_framework import viewsets

from backend.core.models import Birth
from backend.core.serializers import BirthSerializer


class BirthViewSet(viewsets.ModelViewSet):
    queryset = Birth.objects.all()
    serializer_class = BirthSerializer
