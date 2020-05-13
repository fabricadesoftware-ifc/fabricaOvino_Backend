from rest_framework import status, viewsets
from rest_framework.response import Response

from backend.core.models import Birth, Sheep
from backend.core.serializers import BirthCreateSerializer, BirthDetailSerializer, SheepCreateNewbornSerializer


class BirthViewSet(viewsets.ModelViewSet):
    queryset = Birth.objects.all()
    serializer_classes = {"list": BirthDetailSerializer, "create": BirthCreateSerializer}
    default_serializer_class = BirthCreateSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def create(self, request):
        newborns = request.data["newborns"]
        birthday = request.data["birthday"]
        del request.data["newborns"]
        del request.data["birthday"]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        for newborn in newborns:
            newborn["birthday"] = birthday
            newborn_serializer = SheepCreateNewbornSerializer(data=newborn)
            newborn_serializer.is_valid(raise_exception=True)
            self.perform_create(newborn_serializer)
        sheep = Sheep.objects.get(id=request.data["sheep"])
        sheep.pregnant = False
        sheep.save()
        # if request.data["diagnosis"]:
        #     sheep.pregnant = True
        #     sheep.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
