from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Chocolate, ChocolateCategory



# Create your views here.

def all_chocolates(request):
    """
    This view will show all chocolate, along with sorting
    and search queries
    """
    # Stores all items in the chocolate model in a 'chocolates' variable
    chocolates = Chocolate.objects.all()

    # Loads the page with the query variable initially set to 'None' to avoid issues
    query = None

    # Loads the page with the choc_category variable initially set to 'None' to avoid issues
    choc_category_display = None

    # User Search query logic
    if request.GET:

        # Category query used in menu links
        if 'choc_category_display' in request.GET:
            categories = request.GET['choc_category_display'].split(',')
            chocolates = chocolates.filter(choc_category_display__choc_category_name__in=categories)
            categories = ChocolateCategory.objects.filter(choc_category_name__in=categories)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # If query is blank, message is returned, and user is
                # redirected to chocolates url
                messages.error(request, "No search term was entered..")
                return redirect(reverse('chocolates'))

            # If query is valid, uses 'Q' logic to process search
            # ( '|' = or, and 'icontains' makes term case insensitive)
            queries = Q(choc_name__icontains=query) | Q(choc_description__icontains=query)
            chocolates = chocolates.filter(queries)

    context = {
        'chocolates': chocolates,
        'search_term': query,
        'current_categories': categories,
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
