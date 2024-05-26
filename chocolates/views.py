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

    # Loads the page with these query variable initially set
    # to 'None' to avoid issues
    query = None
    categories = None
    sort = None
    direction = None

    # User Search query logic
    if request.GET:

        # Sorting queries used in main-nav
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'choc_name':
                sortkey = 'lower_choc_name'
                products = chocolates.annotate(lower_choc_name=Lower('choc_name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            chocolates = chocolates.order_by(sortkey)

        # Category query used in menu links
        if 'choc_category_display' in request.GET:
            categories = request.GET['choc_category_display'].split(',')
            chocolates = chocolates.filter(
                choc_category_display__choc_category_name__in=categories
            )
            categories = ChocolateCategory.objects.filter(
                choc_category_name__in=categories
            )

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # If query is blank, message is returned, and user is
                # redirected to chocolates url
                messages.error(request, "No search term was entered..")
                return redirect(reverse('chocolates'))

            # If query is valid, uses 'Q' logic to process search
            # ( '|' = or, and 'icontains' makes term case insensitive)
            queries = Q(choc_name__icontains=query) | Q(
                choc_description__icontains=query
            )
            chocolates = chocolates.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'chocolates': chocolates,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
