from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.core.models import Breed, Category, Lots


class Sheep(models.Model):
    class Sex(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

    earringNumber = models.CharField(unique=True, blank=True, null=True, max_length=63)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name="sheeps")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="sheeps")
    lots = models.ForeignKey(
        Lots, on_delete=models.PROTECT, default=None, related_name="sheeps", blank=True, null=True
    )
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.FEMALE)
    teethQuantity = models.IntegerField(default=0)
    birth = models.ForeignKey(
        "Birth", on_delete=models.SET_NULL, related_name="broods", default=None, null=True, blank=True
    )
    pregnant = models.BooleanField(default=False)
    lactating = models.BooleanField(default=False)
