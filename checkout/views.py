from django.shortcuts import render, \
    redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from chocolates.models import Chocolate
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    This view will cache user and transaction
    data during the checkout process and
    determine if the user had the save info
    box checked
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        # DEBUG PRINT STATEMENTS, DELETE BELOW!!!
        print(stripe.api_key)
        print(settings.STRIPE_PUBLIC_KEY)
        print(settings.STRIPE_WH_SECRET)
        print(pid)
        # DEBUG PRINT STATEMENTS, DELETE ABOVE!!!

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    This view will allow the user to complete the checkout
    process and purchase the items in the cart, it also
    contains the logic to implement Stripe functionality
    """

    # Imports the stripe key values from settings.py
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Checks if the request method is 'POST', to handle
    # the submission of the payment
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Populates the order form with the data
        order_form = OrderForm(form_data)

        # If form is valid, it will be saved
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            # Iterate through the cart items to create each line item
            for item_id, item_data in cart.items():
                try:
                    chocolate = Chocolate.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            chocolate=chocolate,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # else:
                    #     for quantity in item_data['items_by_size'].items():
                    #         order_line_item = OrderLineItem(
                    #             order=order,
                    #             product=product,
                    #             quantity=quantity,
                    #             product_size=size,
                    #         )
                    #         order_line_item.save()
                except Chocolate.DoesNotExist:
                    messages.error(request, (
                        "One of the chocolates in your cart wasn't \
                            found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[
                order.order_number
            ]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # Else if request method is 'GET'
    else:
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

        # Prefills form on checkout page with default delivery details
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts, let's customer know
    their payment is complete
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_country': order.country,
                'default_postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
