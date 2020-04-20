from django.db import models

from .sheep import Sheep
from .user import User


class PregnancyDiagnosis(models.Model):
    sheep = models.ForeignKey(Sheep, on_delete=models.PROTECT, related_name="pregnancyDiagnostics")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="pregnancyDiagnostics")
    date = models.DateTimeField()
    diagnosis = models.BooleanField()
