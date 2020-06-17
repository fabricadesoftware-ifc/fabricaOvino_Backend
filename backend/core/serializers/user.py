from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from backend.core.models import User

from .group import GroupUserDetailSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]


class UserCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "username", "name", "groups"]


class UserInfoSerializer(serializers.ModelSerializer):
    groups = GroupUserDetailSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "email", "name", "groups"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "groups"]


class UserPasswordUpdateSerializer(serializers.Serializer):
    model = User

    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "A confirmação de senha não confere!"})
        return super().validate(attrs)
