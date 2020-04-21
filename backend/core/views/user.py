from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.core.models import User
from backend.core.serializers import UserInfoSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return super().get_permissions()

    @action(
        detail=False, url_path="logged",
    )
    @swagger_auto_schema(responses={200: UserSerializer})
    def logged(self, request):
        if not (request.user and request.user.is_authenticated):
            raise PermissionDenied()
        serializer = UserInfoSerializer(self.request.user)
        return Response(serializer.data)
