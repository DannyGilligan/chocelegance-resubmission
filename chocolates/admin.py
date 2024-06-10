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
        'choc_name',
        'choc_dietary_type',
        'choc_category_display',
        'choc_price',
        'choc_image',
    )

    fields = ('choc_friendly_name',
              'choc_name',
              'choc_dietary_type',
              'choc_category_display',
              'choc_description',
              'choc_rating',
              'choc_image',
              'choc_image_url',
              'choc_price',
              'choc_pieces',
              'choc_ingredients',
              'choc_calories',
              'choc_fat',
              'choc_protein',
              'choc_carbs',
              'choc_sugar')

    prepopulated_fields = {"choc_name": ("choc_friendly_name",)}

    ordering = ('choc_name',)


class ChocolateCategoryAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Chocolate Categories'
    """
    list_display = (
        'choc_category_friendly_name',
        'choc_category_dietary_type',
        'choc_category_desc',
    )

    fields = ('choc_category_friendly_name', 'choc_category_desc', 'choc_category_dietary_type', 'choc_category_name')

    prepopulated_fields = {"choc_category_name": ("choc_category_friendly_name",)}


class DietaryTypeAdmin(admin.ModelAdmin):
    """
    Controls the fields displayed to user in the admin
    panel list when viewing 'Dietary Types'
    """
    list_display = (
        'diet_friendly_name',
        'dietary_description',
    )

    fields = ('diet_friendly_name', 'dietary_description', 'dietary_type')

    prepopulated_fields = {"dietary_type": ("diet_friendly_name",)}


admin.site.register(Chocolate, ChocolateAdmin)
admin.site.register(ChocolateCategory, ChocolateCategoryAdmin)
admin.site.register(DietaryType, DietaryTypeAdmin)
