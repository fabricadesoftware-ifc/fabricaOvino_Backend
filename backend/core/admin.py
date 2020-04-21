from django.contrib import admin

from backend.core.models import Breed, Category, PregnancyDiagnosis, Sheep, User

admin.site.register(User)
admin.site.register(Breed)
admin.site.register(Category)
admin.site.register(Sheep)
admin.site.register(PregnancyDiagnosis)
