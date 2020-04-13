from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=255)
