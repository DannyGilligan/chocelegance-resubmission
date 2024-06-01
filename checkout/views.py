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
    process and purchase the items in the cart, it also
    contains the logic to implement Stripe functionality
    """

    # Imports the stripe key values from settings.py
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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

    # Sets the secret key in Stripe
    stripe.api_key = stripe_secret_key

    # Rounds the number to two decimal places for processing payment
    stripe_total = round(total * 100)

    # Creates the payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    # Error message will be displayed if the public key is missing
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did \
            you forget to set it as an environment variable?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
