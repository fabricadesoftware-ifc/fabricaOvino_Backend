from django.db import models

from backend.core.models import Sheep, User


class PregnancyDiagnosis(models.Model):
    sheep = models.ForeignKey(Sheep, on_delete=models.PROTECT, related_name="pregnancy-diagnostics")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="pregnancy-diagnostics")
    date = models.DateTimeField()
    diagnosis = models.BooleanField()
