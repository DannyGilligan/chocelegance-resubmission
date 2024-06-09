from django.contrib import admin
from .models import Testimonial

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
    """
    Registers the Testimonial model in the admin.
    """

    fields = ('testimonial_user', 'testimonial_user_display', 'testimonial_text', 'testimonial_date', 'testimonial_publish')


    list_display = ('testimonial_user_display', 'testimonial_date', 'testimonial_text',)

    ordering = ('-testimonial_date',)  # Most recent first

admin.site.register(Testimonial, TestimonialAdmin)
