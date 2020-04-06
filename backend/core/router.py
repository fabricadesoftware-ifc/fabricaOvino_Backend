from rest_framework.routers import SimpleRouter

from backend.core import views

router = SimpleRouter()

router.register(r"categories", views.CategoryViewSet, basename="category")
