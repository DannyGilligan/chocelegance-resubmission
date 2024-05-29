import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from chocolates.models import Chocolate


class Order(models.Model):
    """
    This model will store the details related to each order
    made by customers. The order history will also be made
    available to the customer to review their activity over
    time.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)  # Unique and permanent
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)  # Not mandatory
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)  # Not mandatory
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets time order is added
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)  # Calculated field
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # Calculated field
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # Calculated field
