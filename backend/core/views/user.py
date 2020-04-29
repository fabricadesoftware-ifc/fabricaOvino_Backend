from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.core.models import User
from backend.core.permissions import IsAdminOrSelf
from backend.core.serializers import (
    UserInfoSerializer,
    UserPasswordUpdateSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = "id"

    queryset = User.objects.all()
    serializer_classes = {"update": UserUpdateSerializer, "password": UserPasswordUpdateSerializer}
    default_serializer_class = UserSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return super().get_permissions()

    def update(self, request, id):
        instance = self.get_object()
        name = request.data.pop("name")
        request.data["first_name"] = name.split(" ")[0]
        request.data["last_name"] = " ".join(name.split(" ")[1:])
        in_serializer = self.get_serializer(instance, data=request.data)
        in_serializer.is_valid(raise_exception=True)
        self.perform_update(in_serializer)
        out_serializer = UserInfoSerializer(instance)

        return Response(out_serializer.data)

    @action(
        detail=False, url_path="logged",
    )
    @swagger_auto_schema(responses={200: UserSerializer})
    def logged(self, request):
        if not (request.user and request.user.is_authenticated):
            raise PermissionDenied()
        serializer = UserInfoSerializer(self.request.user)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], name="password", permission_classes=[IsAdminOrSelf])
    def password(self, request, id=None):
        user = self.get_object()
        serializer = UserPasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            if not (request.user.is_superuser or user.check_password(serializer.data.get("current_password"))):
                return Response({"status": ["Senha atual inválida!"]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data["new_password"])
            user.save()
            return Response({"status": ["Senha alterada com sucesso!"]}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
