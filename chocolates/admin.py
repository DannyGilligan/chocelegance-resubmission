from django.contrib import admin
from .models import Chocolate, ChocolateCategory, DietaryType

# Register your models here.
admin.site.register(Chocolate)
admin.site.register(ChocolateCategory)
admin.site.register(DietaryType)
