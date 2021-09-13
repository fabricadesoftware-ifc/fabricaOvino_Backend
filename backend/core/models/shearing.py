from django.db import models
from .sheep import Sheep
from .user import User

class Shearing(models.Model): #classe tosquiar 
    sheep = models.ForeignKey(Sheep, on_delete=models.PROTECT, related_name="shearing")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="shearing")
    date = models.DateField()
    amountOfWool =  models.FloatField() #Quantidade de lã
