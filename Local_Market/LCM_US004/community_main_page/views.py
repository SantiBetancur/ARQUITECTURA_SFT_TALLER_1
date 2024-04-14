from django.shortcuts import render,redirect, get_object_or_404
from .models import products
# I am use the Q class to realize the request of the search
from django.db.models import Q
from django.contrib.auth import logout, get_user
from Sellerprofile.models import Seller
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    search_query = request.GET.get("search")
    products_queryset = products.objects.all()

    if search_query:
       
            # Si el valor de búsqueda no es un número, busca coincidencias parciales en los campos 'name' y 'description'
            products_queryset = products_queryset.filter(
                Q(name__icontains=search_query) |
                Q(price__icontains=search_query)
            )

    context = {
        'dataset': products_queryset
    }

    user = get_user(request)
    user_instance = None
    if user.is_authenticated:
        user_instance = User.objects.get(id = user.id)
        context['session_user'] = user_instance.username
        is_seller = Seller.objects.filter(user_info = user_instance).exists()
        context['is_seller'] = is_seller
    return render(request, "home.html", context)

def prod_detail(request, product_id):
        product = get_object_or_404(products, pk = product_id)
        context = {}
        context['dataset'] = product
        user = get_user(request)
        current_user = ""
        if user.is_authenticated:
            current_user = user
            context['session_user'] = current_user.username
            return render(request, 'product_detail.html', context)
        
def user_logout(request):
    logout(request)
    return redirect('/')