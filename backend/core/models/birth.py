from django.db import models

from .user import User


class Birth(models.Model):
    sheep = models.ForeignKey("Sheep", on_delete=models.PROTECT, related_name="births")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="births")
    date = models.DateTimeField()
    newborns_quantity = models.IntegerField()
    observations = models.TextField()
