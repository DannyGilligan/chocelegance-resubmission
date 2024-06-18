from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


# Custom Model 1
class DietaryType(models.Model):
    """
    The DietaryType model will hold the values for the various
    dietary types that are catered to by Chocelegance along with
    their descriptions (e.g, Keto, Vegan, Gluten-Free etc)
    """
    dietary_type = models.SlugField(
        default="",
        max_length=200,
        null=True,
        blank=True
        )

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

    class Meta:
        """
        Model name to be displayed in admin panel
        (capitalises 'Types' for consistency)
        """
        verbose_name_plural = "Dietary Types"


# Custom Model 2
class ChocolateCategory(models.Model):
    """
    The ChocolateCategory model will hold the values for the various
    chocolate categories offered by Chocelegance and their description
    (e.g, Dark Chocolate, Milk Chocolate and White Chocolate etc)
    """
    choc_category_name = models.SlugField(
        default="", max_length=200, null=True, blank=True
    )
    choc_category_friendly_name = models.CharField(
        max_length=200, null=True, blank=True
    )
    choc_category_desc = models.TextField()
    choc_category_dietary_type = models.ForeignKey(
        'DietaryType', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        """
        This function returns the model name for easier readibility in
        the admin panel
        """
        return self.choc_category_name

    def get_choc_friendly_name(self):
        """
        This function returns the friendly name for easier readibility
        where needed
        """
        return self.choc_category_friendly_name

    class Meta:
        """
        Model name to be displayed in admin panel
        """
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
        'DietaryType',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )

    choc_category_display = models.ForeignKey(
        'ChocolateCategory',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )

    choc_name = models.SlugField(
        default="",
        max_length=200,
        null=True,
        blank=False
    )

    choc_friendly_name = models.CharField(
        max_length=200, null=True, blank=False
    )

    choc_description = models.TextField()

    choc_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    choc_image = models.ImageField(
        null=True, blank=True
    )

    choc_image_url = models.URLField(
        max_length=2000, null=True, blank=True
    )

    choc_price = models.DecimalField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2,
        blank=False
    )

    choc_pieces = models.PositiveIntegerField(
        blank=True,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    choc_ingredients = models.TextField()

    choc_calories = models.PositiveIntegerField(
        blank=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )

    choc_fat = models.PositiveIntegerField(
        blank=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )

    choc_protein = models.PositiveIntegerField(
        blank=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )

    choc_carbs = models.PositiveIntegerField(
        blank=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )

    choc_sugar = models.PositiveIntegerField(
        blank=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )

    def get_choc_rating(self):
        """
        This function will calculate the rating for each chocolate
        by accessing the ChocolateReview model (using the related name
        choc_reviews) and summing up the ratings, then dividing by
        the count of ratings
        """

        choc_reviews_total = 0

        # 'choc_reviews' is the related name of the
        # ChocolateReview model, where the ratings are stored
        for review in self.choc_reviews.all():
            choc_reviews_total += review.choc_rating

        if self.choc_reviews.count() > 0:
            self.choc_rating = choc_reviews_total / self.choc_reviews.count()
            return choc_reviews_total / self.choc_reviews.count()

        return 0

    def save(self, *args, **kwargs):
        """
        This function overrides the save method to update
        the choc_rating value with the calculated value
        after reviews submissions
        """
        self.choc_rating = self.get_choc_rating()
        super(Chocolate, self).save(*args, **kwargs)

    def __str__(self):
        """
        This function returns the model name for easier readibility in
        the admin panel
        """
        return self.choc_name


# Custom Model 4

class ChocolateReview(models.Model):
    """
    This ChocolateReview model will hold the reviews and ratings on
    the chocolates left by users of the site
    """

    CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    # Chocolate as a foreign key from the Chocolate model
    chocolate = models.ForeignKey(
        Chocolate, related_name="choc_reviews",
        on_delete=models.CASCADE
        )

    # Ratings will be an integer, defaulting to 3 (range 1 to 5)
    choc_rating = models.IntegerField(null=True, blank=True, default=3)

    # The text content of the review
    review_content = models.TextField(null=True, blank=True)

    # The user who left the review
    created_by_user = models.ForeignKey(
        User, related_name="choc_reviews",
        on_delete=models.CASCADE
        )

    # The date the review was left
    created_date = models.DateTimeField(auto_now_add=True)

    # Publish to site will default to 'No'
    # in order to allow for admin approval
    publish_review = models.CharField(
        null=True,
        blank=True,
        max_length=3,
        choices=CHOICES,
        default="No"
    )
