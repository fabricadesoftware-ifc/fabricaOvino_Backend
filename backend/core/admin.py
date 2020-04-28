from django.contrib import admin
from django.contrib.auth.models import ContentType, Permission

from backend.core.models import Breed, Category, PregnancyDiagnosis, Sheep, User

admin.site.register(User)
admin.site.register(Breed)
admin.site.register(Category)
admin.site.register(ContentType)
admin.site.register(Sheep)
admin.site.register(Permission)
admin.site.register(PregnancyDiagnosis)
