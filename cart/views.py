from django.shortcuts import render, redirect, reverse

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

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    This view will allow the user to adjust/remove the
    quantity of items in the cart
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

