from django.db import models
from .sheep import Sheep


class Lots(models.Model):
    name = models.CharField(max_length=255, default=None)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name
