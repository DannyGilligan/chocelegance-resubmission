from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from chocolates.models import Chocolate


def cart_contents(request):
    """
    This function returns a dictionary and stores it in the
    context variable, this context can then be accessed by
    all templates across the entire site by adding it to
    the templates variable in settings.py
    """

    cart_items = []
    total = 0
    chocolate_count = 0
    cart = request.session.get('cart',{})

    for item_id, quantity in cart.items():
        chocolate = get_object_or_404(Chocolate, pk=item_id)
        total += quantity * chocolate.choc_price
        chocolate_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'chocolate': chocolate,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'chocolate_count': chocolate_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context