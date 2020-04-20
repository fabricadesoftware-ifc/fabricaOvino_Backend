from django.contrib import admin

from backend.core.models import Breed, Category, Sheep, User

admin.site.register(User)
admin.site.register(Breed)
admin.site.register(Category)
admin.site.register(Sheep)
