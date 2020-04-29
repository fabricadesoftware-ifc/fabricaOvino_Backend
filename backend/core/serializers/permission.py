from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source="content_type.__str__", read_only=True)

    class Meta:
        model = Permission
        fields = ["id", "name", "content_type"]
