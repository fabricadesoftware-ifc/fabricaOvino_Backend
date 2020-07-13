from django.db.models.deletion import ProtectedError
from rest_framework import status, viewsets
from rest_framework.response import Response

from backend.core.models import Category
from backend.core.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    lookup_field = "id"

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

    def destroy(self, request, id):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(
                status=status.HTTP_423_LOCKED,
                data={"detail": "Objeto protegido. Esta categoria já está atribuída a algum animal."},
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
