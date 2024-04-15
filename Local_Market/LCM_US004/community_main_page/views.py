from django.shortcuts import render,redirect, get_object_or_404
from .models import products
from .models import ProductUser
# I am use the Q class to realize the request of the search
from django.db.models import Q
from django.contrib.auth import logout, get_user
from Sellerprofile.models import Seller
from django.contrib.auth.models import User
from django.db.models import Count
from django.urls import reverse

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
        
        if is_seller:
            seller_instance = Seller.objects.get(user_info = user_instance)
            context['seller_id'] = seller_instance.id
            context['seller_name'] = seller_instance.name
    return render(request, "home.html", context)

def prod_detail(request, product_id):
        product = get_object_or_404(products, pk = product_id)
        context = {}
        context['dataset'] = product
        user = get_user(request)

        user_instance = None
        has_duplicates = False
        if user.is_authenticated:
            user_instance = User.objects.get(id = user.id)
            context['session_user'] = user_instance.username
            existing_fav = ProductUser.objects.filter(user_info_id = user_instance, product_info_id = product_id).annotate(count=Count('id'))
            has_duplicates = len(existing_fav) > 0
            
            
            if request.method == 'POST' and has_duplicates == False:
                new_instance = ProductUser()
                user_id = User.objects.get(id = user.id)
                new_instance.user_info = user_id
                current_product = products.objects.get(pk = product_id)
                new_instance.product_info = current_product
                new_instance.save()
                return redirect(f'/available_communities/EAFIT/products/details/{product_id}')
            context['seller_id'] = product.seller_info.id
            context['has_duplicates'] = has_duplicates
            return render(request, 'product_detail.html', context)
            
            
        
def user_logout(request):
    logout(request)
    return redirect('/')