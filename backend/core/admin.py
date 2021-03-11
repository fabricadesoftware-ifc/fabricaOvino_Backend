from django.contrib import admin

from backend.core.models import Birth, Breed, Category, Lots, PregnancyDiagnosis, Shearing, Sheep, User

# from django.contrib.auth.models import ContentType, Permission


admin.site.register(User)
admin.site.register(Birth)
admin.site.register(Breed)
admin.site.register(Category)
admin.site.register(Lots)
admin.site.register(Sheep)
admin.site.register(PregnancyDiagnosis)
admin.site.register(Shearing)
