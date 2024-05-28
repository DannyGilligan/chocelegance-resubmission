from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from chocolates.models import Chocolate
# Create your views here.


def view_cart(request):
    """
    This view will return the shopping cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    This view will allow the user to add a quantity
    of a particular product to the cart
    """

    chocolate = get_object_or_404(Chocolate, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {chocolate.choc_friendly_name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{chocolate.choc_friendly_name} has been added to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    This view will allow the user to adjust the
    quantity of items in the cart
    """

    chocolate = get_object_or_404(Chocolate, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {chocolate.choc_friendly_name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'{chocolate.choc_friendly_name} has been removed from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    This view will allow the user to remove
    items from the cart entirely
    """

    try:
        chocolate = get_object_or_404(Chocolate, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'{chocolate.choc_friendly_name} has been removed from your cart')

        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        # Error message below will be displayed
        # to avoid the view failing fail_silently
        messages.error(request, f'Error encountered while removing item: {e}')
        return HttpResponse(status=500)


