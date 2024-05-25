from django.contrib import admin
from .models import Chocolate, ChocolateCategory, DietaryType

# Register your models here.

class ChocolateAdmin(admin.ModelAdmin):
    list_display = (
        'choc_name',
        'choc_dietary_type',
        'choc_category',
        'choc_price',
        
        'choc_image',
    )

    ordering = ('choc_name',)


class ChocolateCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'choc_category_desc',
    )


class DietaryTypeAdmin(admin.ModelAdmin):
    list_display = (
        'dietary_description',
    )




admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(ChocolateCategory, ChocolateCategoryAdmin)
admin.site.register(DietaryType, DietaryTypeAdmin)


