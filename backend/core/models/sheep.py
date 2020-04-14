from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.core.models import Breed, Category


class Sheep(models.Model):
    class Sex(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

    earringNumber = models.CharField(unique=True, blank=True, null=True, max_length=63)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name="sheeps")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="sheeps")
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.FEMALE)
    teethQuantity = models.IntegerField()
    mother = models.ForeignKey("self", related_name="mother_children", on_delete=models.PROTECT, blank=True, null=True)
    father = models.ForeignKey("self", related_name="father_children", on_delete=models.PROTECT, blank=True, null=True)
