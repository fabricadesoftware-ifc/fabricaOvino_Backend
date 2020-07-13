from django.db.models.deletion import ProtectedError
from rest_framework import status, viewsets
from rest_framework.response import Response

from backend.core.models import Sheep
from backend.core.serializers import SheepDetailSerializer, SheepSerializer


class SheepViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Sheep.objects.all()
    serializer_classes = {
        "list": SheepDetailSerializer,
    }
    default_serializer_class = SheepSerializer

    def get_queryset(self):
        pregnant = self.request.query_params.get("pregnant", None)
        if pregnant == "True":
            queryset = Sheep.objects.filter(pregnant=True)
        elif pregnant == "False":
            queryset = Sheep.objects.filter(pregnant=False)
        else:
            queryset = Sheep.objects.all()
        return queryset

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def destroy(self, request, id):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(
                status=status.HTTP_423_LOCKED,
                data={"detail": "Objeto protegido. Este animal já está atribuída a alguma outra função."},
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
