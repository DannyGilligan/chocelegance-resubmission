import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from chocolates.models import Chocolate
from profiles.models import UserProfile


class Order(models.Model):
    """
    This model will store the details related to each order
    made by customers. The order history will also be made
    available to the customer to review their activity over
    time.
    """

    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )  # Unique and permanent
    # Pulls in the user data from the UserProfile model
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(
        max_length=20, null=True, blank=True
    )  # Not mandatory
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(
        max_length=80, null=True, blank=True
    )  # Not mandatory
    date = models.DateTimeField(
        auto_now_add=True
    )  # Automatically sets time order is added
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )  # Calculated field
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )  # Calculated field
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )  # Calculated field
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
        Private method (denoted by underscore), used only by the Order model.
        This will generate a random, unique order number using UUID package.
        """
        return uuid.uuid4().hex.upper()  # String of 32 characters as order no.

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """

        # Uses sum function for each line item total fields in the order
        self.order_total = self.lineitems.aggregate(Sum("lineitem_total"))[
            "lineitem_total__sum"
        ] or 0  # Sets to 0 instead of none if empty, causes error otherwise

        # Delivery total is calculated below
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0

        # Grand total is calculated below (sum of order total & delivery cost)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            # If order does not have an order number,
            # the _generate_order_number method will be called
            # and the order number will be saved to the oder_number
            # variable below.
            self.order_number = self._generate_order_number()

        # Once the order number is generated, it will be saved.
        super().save(*args, **kwargs)

    # Returns the order number to display in the admin panel
    def __str__(self):
        return self.order_number

    # Sorts the orders by most recent first
    class Meta:
        ordering = ['-date']


class OrderLineItem(models.Model):
    """
    This model will store details regarding each
    individual line item in an order. This will form
    the basis of calculating the delivery cost, order total
    and grand total of the order as a whole.
    """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    chocolate = models.ForeignKey(
        Chocolate, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )  # Calculated field

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """

        # Multiplies the quantity by the price to arrive
        # at a line item total
        self.lineitem_total = self.chocolate.choc_price * self.quantity
        super().save(*args, **kwargs)

    # Returns the chocolate name and the order number for each order line item
    def __str__(self):
        return f"{self.chocolate.choc_friendly_name} on \
        order {self.order.order_number}"
