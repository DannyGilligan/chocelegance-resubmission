from django.shortcuts import render, get_object_or_404
from .models import Chocolate

# Create your views here.

def all_chocolates(request):
    """
    This view will show all chocolate, along with sorting
    and search queries
    """

    chocolates = Chocolate.objects.all()

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
        'chocolate': chocolates,
    }
    
    return render(request, 'chocolates/chocolate_detail.html', context)
