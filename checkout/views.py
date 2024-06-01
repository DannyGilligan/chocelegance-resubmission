from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

# Create your views here.


def checkout(request):
    """
    This view will allow the user to complete the checkout
    process and purchase the items in the cart
    """
    
    # Cart contents are stored in the cart variable
    cart = request.session.get('cart', {})

    # If the cart is empty, the code below will execute
    if not cart:
        messages.error(request, "Your cart is empty at the moment!")
        # Customer is redirected back to the chocolates page
        return redirect(reverse('chocolates'))


    # Gets the cart values from the cart_contents view
    current_cart = cart_contents(request)

    # Gets the total by accessing the grand total key
    total = current_cart['grand_total']

    # Rounds the number to two decimal places for processing payment
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'fake_key',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)