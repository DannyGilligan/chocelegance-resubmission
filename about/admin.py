from django.contrib import admin

# Register your models here.

class FaqAdmin(admin.ModelAdmin):
    """
    Registers the FAQ model in the admin.
    """

    fields = ('faq_question', 'faq_answer', 'faq_publish')

    list_display = ('faq_question', 'faq_publish',)

    ordering = ('faq_publish',)  # Published FAQs shown first


admin.site.register(FaqAdmin)