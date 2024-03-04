from django.shortcuts import render
from .models import products
# I am use the Q class to realize the request of the search
from django.db.models import Q

# Create your views here.

def home(request):

    # To realize the search 
    search = request.GET.get("search")
    product = products.objects.all()
    if (search):
        product = product.filter(
            Q(name = search) |
            Q(price = search)
        ).distinct()
    context = {}
    context['dataset'] = product
    return render(request, "home.html", context)
