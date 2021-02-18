from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def name(self):
        return " ".join((self.first_name, self.last_name))

    @name.setter
    def name(self, value):
        self.first_name = value.split(" ")[0]
        self.last_name = " ".join(value.split(" ")[1:])
