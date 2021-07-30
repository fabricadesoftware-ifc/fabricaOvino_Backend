from django.db import models
from .feed import Feed
from .sheep import Sheep
from .user import User


class Weight(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.PROTECT, blank=True, null=True, related_name="weights")
    sheep = models.ForeignKey(Sheep, on_delete=models.PROTECT, related_name="weights")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="weights")
    date = models.DateField()
    observations = models.TextField(blank=True)
    weight = models.FloatField(default=0)
