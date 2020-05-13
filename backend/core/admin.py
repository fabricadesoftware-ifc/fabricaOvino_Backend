from django.contrib import admin

from backend.core.models import Birth, Breed, Category, PregnancyDiagnosis, Sheep, User

# from django.contrib.auth.models import ContentType, Permission


admin.site.register(User)
admin.site.register(Birth)
admin.site.register(Breed)
admin.site.register(Category)
admin.site.register(Sheep)
admin.site.register(PregnancyDiagnosis)
