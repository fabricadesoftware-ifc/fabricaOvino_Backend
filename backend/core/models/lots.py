from django.db import models
from .sheep import Sheep

from .user import User


class Lots(models.Model):
    sheep = models.ForeignKey(Sheep, on_delete=models.PROTECT, related_name="lots")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="lots")
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
