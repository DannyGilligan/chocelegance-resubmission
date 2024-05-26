from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Chocolate
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def all_chocolates(request):
    """
    This view will show all chocolate, along with sorting
    and search queries
    """

    chocolates = Chocolate.objects.all()

    # User Search query logic
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # If query is blank, message is returned, and user is
                # redirected to chocolates url
                messages.error(request, "No search term was entered..")
                return redirect(reverse('chocolates'))

            # If query is valid, uses 'Q' logic to process search
            # ( '|' = or, and 'icontains' makes term case insensitive)
            queries = Q(name_icontains=query) | Q(description_icontains=query)

    context = {
        'chocolates': chocolates,
    }

    return render(request, 'chocolates/chocolates.html', context)


def chocolate_detail(request, chocolate_id):
    """
    This view will render the details for an individual chocolate
    based on the chocolate id
    """

    chocolate = get_object_or_404(Chocolate, pk=chocolate_id)

    context = {
        'chocolate': chocolate,
    }

    return render(request, 'chocolates/chocolate_detail.html', context)
