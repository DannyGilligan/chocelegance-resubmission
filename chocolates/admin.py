from django.contrib import admin
from .models import Chocolate, ChocolateCategory, DietaryType

# Register your models here.

class ChocolateAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Chocolates'
    """
    list_display = (
        'choc_name',
        'choc_dietary_type',
        'choc_category',
        'choc_price',
        
        'choc_image',
    )

    ordering = ('choc_name',)


class ChocolateCategoryAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Chocolate Categories'
    """
    list_display = (
        'choc_category',
        'choc_category_desc',
    )


class DietaryTypeAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Dietary Types'
    """
    list_display = (
        'dietary_type',
        'dietary_description',
    )




admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(ChocolateCategory, ChocolateCategoryAdmin)
admin.site.register(DietaryType, DietaryTypeAdmin)

