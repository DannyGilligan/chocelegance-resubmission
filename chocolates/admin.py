from django.contrib import admin
from .models import Chocolate, ChocolateCategory, DietaryType

# Register your models here.


class ChocolateAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Chocolates'
    """
    list_display = (
        'choc_friendly_name',
        'choc_dietary_type',
        'choc_category_display',
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
        'choc_friendly_name',
        'choc_category_desc',
        'choc_category_dietary_type',
    )

    prepopulated_fields = {"slug": ("choc_friendly_name")}


class DietaryTypeAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Dietary Types'
    """
    list_display = (
        'diet_friendly_name',
        'dietary_description',
    )


admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(ChocolateCategory, ChocolateCategoryAdmin)
admin.site.register(DietaryType, DietaryTypeAdmin)
