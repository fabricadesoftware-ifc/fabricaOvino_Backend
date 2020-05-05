from django.contrib.auth.models import Permission
from django.db.models import Q
from rest_framework import mixins, viewsets

from backend.core.serializers import PermissionSerializer


class PermissionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # queryset = Permission.objects.all()
    queryset = Permission.objects.filter(
        Q(content_type__app_label="auth", content_type__model="group") | Q(content_type__app_label="core")
    )

    serializer_class = PermissionSerializer
