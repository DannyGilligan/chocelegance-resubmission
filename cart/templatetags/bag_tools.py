from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    This function will calculate the
    subtotal amount to be shown on the checkout page
    """
    return price * quantity

# Code validated in CI Python Linter, no errors
