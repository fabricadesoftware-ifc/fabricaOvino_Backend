from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
