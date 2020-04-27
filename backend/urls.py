from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.core.router import router

schema_view = get_schema_view(openapi.Info(title="Ovinocultura", default_version="v1"), public=True)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/v1/refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
    path("admin/", admin.site.urls),
    path("swagger/", schema_view.with_ui()),
]
