from django.db import models

# Create your models here.

# Custom Model 4


class Faq(models.Model):
    """
    The FAQ model will hold all the questions and answers
    that will be injected into the about template (If the
    faq_publish field is set to "Yes"). The content will
    be updated directly from the admin panel by the
    superuser
    """

    CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    faq_question = models.CharField(
        max_length=500, null=False, blank=False
        )

    faq_answer = models.TextField()

    faq_publish = models.CharField(
        null=False,
        blank=False,
        max_length=3,
        choices=CHOICES
    )

    def __str__(self):
        """
        This function returns the model name for easier readibility
        in the admin panel
        """
        return self.faq_question

    class Meta:
        """
        Model name to be displayed in admin panel
        """
        verbose_name_plural = "FAQs"
