from django.contrib.auth.models import Group
from rest_framework import serializers

from .permission import PermissionSerializer


class GroupSerializer(serializers.ModelSerializer):
    # permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]


class GroupDetailSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]
