from backend.core import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r"births", views.BirthViewSet, basename="birth")
router.register(r"breeds", views.BreedViewSet, basename="breed")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"feeds", views.FeedViewSet, basename="feed")
router.register(r"groups", views.GroupViewSet, basename="group")
router.register(r"lots", views.LotsViewSet, basename="lots")
router.register(r"permissions", views.PermissionViewSet, basename="permission")
router.register(r"pregnancy-diagnosis", views.PregnancyDiagnosisViewSet, basename="pregnancy-diagnosis")
router.register(r"shearing", views.ShearingViewSet, basename="shearing")
router.register(r"sheeps", views.SheepViewSet, basename="sheep")
router.register(r"users", views.UserViewSet, basename="user")
