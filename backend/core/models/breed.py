from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100, blank=True, null=True, default=None)
