from django.db import models

# Create your models here.

class DietaryType(models.Model):
    """
    The DietaryType model will hold the values for the various
    dietary types that are catered to by Chocelegance along with
    their descriptions (e.g, Keto, Vegan, Gluten-Free etc)
    """
    dietary_type = models.CharField(max_length=200)
    dietary_description = models.TextField
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        """
        This function returns the model name for easier readibility in the admin panel
        """
        return self.name

    def get_friendly_name(self):
        """
        This function returns the friendly name for easier readibility where needed
        """
        return self.friendly_name
        
