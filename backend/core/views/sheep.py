from rest_framework import viewsets

from backend.core.models import Sheep
from backend.core.serializers import SheepDetailSerializer, SheepSerializer


class SheepViewSet(viewsets.ModelViewSet):
    queryset = Sheep.objects.all()
    serializer_classes = {
        "list": SheepDetailSerializer,
    }
    default_serializer_class = SheepSerializer

    def get_queryset(self):
        pregnant = self.request.query_params.get("pregnant", None)
        print("Oi")
        print(pregnant)
        if pregnant is not None:
            queryset = Sheep.objects.filter(pregnant=True)
        else:
            queryset = Sheep.objects.all()
        return queryset

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
