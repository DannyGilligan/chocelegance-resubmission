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
    diet_friendly_name = models.CharField(
        max_length=200, null=True, blank=True
    )

    def __str__(self):
        """
        This function returns the model name for easier readibility
        in the admin panel
        """
        return self.dietary_type

    def get_friendly_name(self):
        """
        This function returns the friendly name for easier readibility
        where needed
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
        This function returns the model name for easier readibility in
        the admin panel
        """
        return self.choc_category

    class Meta:
        verbose_name_plural = "Chocolate Categories"


# Custom Model 3
class Chocolate(models.Model):
    """
    The Chocolate Model will hold the details for all chocolates sold
    by Chocelegance. This includes all the necessary details that
    customers expect, such as price, description, image, ingredients,
    macro-nutrional values etc.
    """
    choc_dietary_type = models.ForeignKey(
        'DietaryType', null=True, blank=True, on_delete=models.SET_NULL
    )
    choc_category = models.ForeignKey(
        'ChocolateCategory', null=True, blank=True, on_delete=models.SET_NULL
    )
    choc_name = models.CharField(max_length=200)
    choc_description = models.TextField()
    choc_image = models.ImageField(null=True, blank=True)
    choc_image_url = models.URLField(max_length=2000, null=True, blank=True)
    choc_price = models.FloatField()
    choc_ingredients = models.TextField()
    choc_fat = models.FloatField()
    choc_protein = models.FloatField()
    choc_carbs = models.FloatField()
    choc_sugar = models.FloatField()

    def __str__(self):
        """
        This function returns the model name for easier readibility in
        the admin panel
        """
        return self.choc_name

