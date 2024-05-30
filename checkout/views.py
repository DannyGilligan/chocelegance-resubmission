from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

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

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)