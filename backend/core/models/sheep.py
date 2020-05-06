from django.db import models

from backend.core.models import Birth, Breed, Category


class Sheep(models.Model):
    class Sex(models.TextChoices):
        FEMALE = "F", "Female"
        MALE = "M", "Male"

    earringNumber = models.CharField(unique=True, blank=True, null=True, max_length=63)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name="sheeps")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="sheeps")
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.FEMALE)
    teethQuantity = models.IntegerField()
    birth = models.ForeignKey(Birth, on_delete=models.PROTECT, related_name="broods")
