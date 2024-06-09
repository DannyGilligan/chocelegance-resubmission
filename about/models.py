from django.db import models

# Create your models here.

# Custom Model 1
class faq(models.Model):
    """
    The FAQ model will hold all the questions and answers
    that will be injected into the about template (If the
    faq_publish field is set to "Yes"). The content will
    be updated directly from the admin panel by the
    superuser
    """

    CHOICES = (
        ("Yes", "Yes"),
        ("No", "Yes"),
    )

    faq_question = models.CharField(max_length=500)
    faq_answer = models.TextField()
    faq_publish = models.CharField(
        max_length=3, choices=CHOICES
    )

    def __str__(self):
        """
        This function returns the model name for easier readibility
        in the admin panel
        """
        return self.faq

    def get_friendly_name(self):
        """
        This function returns the friendly name for easier readibility
        where needed
        """
        return self.friendly_name

    class Meta:
        """
        Model name to be displayed in admin panel
        """
        verbose_name_plural = "FAQs"