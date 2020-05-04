from django.contrib.auth.models import Group
from rest_framework import viewsets

from backend.core.serializers import GroupDetailSerializer, GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_classes = {
        "list": GroupDetailSerializer,
    }
    default_serializer_class = GroupSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
