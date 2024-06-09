from django.db import models

# Create your models here.

# Custom model 5

class Testimonial(models.Model):
    """
    The Testimonial model will hold all the testimonials
    received by customers and inject them into the index.html
    page (if the 'testimonial_publish field is set to "Yes).
    that will be injected into the about template (If the
    The content will be updated directly from the admin
    panel by the superuser
    """

    CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    testimonial_user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimonial_user_display = models.CharField(max_length=50, null=False, blank=False)
    testimonial_text = models.TextField()
    testimonial_date = models.DateField(null=False, blank=False)
    testimonial_publish = models.CharField(null=False, blank=False, max_length=3, choices=CHOICES)

    def __str__(self):
        """
        This function returns the model name for easier readibility
        in the admin panel
        """
        return self.testimonial_user_display

    class Meta:
        """
        Model name to be displayed in admin panel
        """
        verbose_name_plural = "Customer Testimonials"
