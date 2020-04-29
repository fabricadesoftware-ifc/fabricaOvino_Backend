from django.contrib.auth.models import Group
from rest_framework import serializers

from .permission import PermissionSerializer


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]
