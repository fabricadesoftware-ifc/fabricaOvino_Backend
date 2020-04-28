from django.contrib.auth.models import Permission
from rest_framework import mixins, viewsets

from backend.core.serializers import PermissionSerializer


class PermissionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
