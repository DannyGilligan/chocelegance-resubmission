from django.shortcuts import render
from .models import Chocolate

# Create your views here.

def AllChocolates(request):
    """
    This view will show all chocolate, along with sorting
    and search queries
    """

    chocolates = Chocolate.objects.all()

    context = {
        'chocolates': chocolates,
    }
    return render(request, 'chocolates/chocolates.html', context)
