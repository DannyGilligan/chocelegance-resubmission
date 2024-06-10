from django.contrib import admin
from .models import Faq

# Register your models here.


class FaqAdmin(admin.ModelAdmin):
    """
    Registers the FAQ model in the admin.
    """

    fields = ('faq_question', 'faq_answer', 'faq_publish')

    list_display = ('faq_question', 'faq_publish',)


admin.site.register(Faq, FaqAdmin)
