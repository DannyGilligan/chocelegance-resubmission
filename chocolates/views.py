from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Chocolate, ChocolateCategory
from .forms import ChocolateForm
from django.contrib.auth.decorators import login_required  # Provides security layer!


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

            # Sort by choc_name
            if sortkey == 'choc_name':
                sortkey = 'lower_choc_name'
                chocolates = chocolates.annotate(
                    lower_choc_name=Lower('choc_name')
                )

            # Sort by choc category (Dark, Milk, White etc)
            if sortkey == 'choc_category_display':
                sortkey = 'choc_category_display__choc_category_name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            chocolates = chocolates.order_by(sortkey)

        # Category query used in menu links to view entire categories
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


@login_required
def add_chocolate(request):
    """
    This view allows superuser to add chocolates to the model/database
    """

    if request.method == 'POST':
        # FILES allows image to be captures
        form = ChocolateForm(request.POST, request.FILES)
        if form.is_valid():
            chocolate = form.save()
            messages.success(request, 'Chocolate added!')
            # Redirect user to the detail page of the chocolate they just added
            return redirect(reverse('chocolate_detail', args=[chocolate.id]))
        else:
            messages.error(request, 'Failed to add Chocolate.\
            Please ensure the form is valid.')
    else:
        form = ChocolateForm()

    template = 'chocolates/add_chocolate.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_chocolate(request, chocolate_id):
    """
    This view allows superuser to edit chocolates in the model/database
    """

    # Stores the selected chocolate from
    # the Chocolate model in a 'chocolate' variable
    chocolate = get_object_or_404(Chocolate, pk=chocolate_id)

    # When submit button is clicked, the POST logic below will be triggered
    if request.method == 'POST':
        form = ChocolateForm(request.POST, request.FILES, instance=chocolate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved successfully!')
            return redirect(reverse('chocolate_detail', args=[chocolate.id]))
        else:
            messages.error(request, 'Changes not saved. \
            Please ensure that the entered details are valid.')
    else:
        # Insantiates a Chocolate Form using the
        # selected Chocolate in the 'chocolate' variable
        # Result is a prefilled form
        form = ChocolateForm(instance=chocolate)

        # Lets user know they're about to edit a chocolate
        messages.info(request, f'You are about to \
        edit {chocolate.choc_friendly_name}')

    template = 'chocolates/edit_chocolate.html'
    context = {
        'form': form,
        'chocolate': chocolate,
    }

    return render(request, template, context)

    if request.method == 'POST':
        # FILES allows image to be captures
        form = ChocolateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chocolate added!')
            # Redirect user back to add_chocolate view
            return redirect(reverse('add_chocolate'))
        else:
            messages.error(request, 'Failed to add Chocolate. \
            Please ensure the form is valid.')
    else:
        form = ChocolateForm()

    template = 'chocolates/add_chocolate.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def delete_chocolate(request, chocolate_id):
    """
    This view will allow superuser to delete chocolates from the model/database
    """

    chocolate = get_object_or_404(Chocolate, pk=chocolate_id)
    chocolate.delete()
    messages.success(request, 'Chocolate has been deleted!')
    return redirect(reverse('chocolates'))
