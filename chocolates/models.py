from django.db import models



# Custom Model 1
class DietaryType(models.Model):
    """
    The DietaryType model will hold the values for the various
    dietary types that are catered to by Chocelegance along with
    their descriptions (e.g, Keto, Vegan, Gluten-Free etc)
    """
    dietary_type = models.CharField(max_length=200)
    dietary_description = models.TextField()
    diet_friendly_name = models.CharField(max_length=200, null=True, blank=True)

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
        

# Custom Model 2
class ChocolateCategory(models.Model):
    """
    The ChocolateCategory model will hold the values for the various
    chocolate categories offered by Chocelegance and their description
    (e.g, Dark Chocolate, Milk Chocolate and White Chocolate etc)
    """
    choc_category = models.CharField(max_length=200)
    choc_category_desc = models.TextField()

    def __str__(self):
        """
        This function returns the model name for easier readibility in the admin panel
        """
        return self.name
