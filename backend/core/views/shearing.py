from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from backend.core.models import Shearing, Sheep
from backend.core.serializers import ShearingSerializer, ShearingDetailSerializer

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

    def partial_update(self, request, id):
        instance = self.get_object()
        in_serializer = ShearingDetailSerializer(instance, data=request.data)
        in_serializer.is_valid(raise_exception=True)
        self.perform_update(in_serializer)
        out_serializer = ShearingDetailSerializer(instance)

        return Response(out_serializer.data)

class ShearingEarringNumber(mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = "id"
    queryset = Shearing.objects.all()
    serializer_class = ShearingDetailSerializer

    def get(self):
        sheeps = Sheep.objects.all()
        result = []

        for shearing in self.get_queryset():
            for sheep in sheeps:
                if shearing.sheep == sheep.id:
                    shearing.sheep = sheep.earringNumber
                    serializer = self.get_serializer(shearing)
                    result.append(serializer.data)

        return Response(result, status.HTTP_200_OK)
