from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 
                       'delivery_cost', 'order_total',
                       'grand_total',)


