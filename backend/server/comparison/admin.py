from django.contrib import admin
from .models import PhoneData, CategoryChoices, BrandChoices, ModelChoices
# Register your models here.


admin.site.register(CategoryChoices)
admin.site.register(BrandChoices)
admin.site.register(ModelChoices)

admin.site.register(PhoneData)
