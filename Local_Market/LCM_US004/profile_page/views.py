from django.shortcuts import render
from django.contrib.auth import logout, get_user
from django.db.models import Q
from community_main_page.models import products,ProductUser
from django.contrib.auth.models import User


# Create your views here.

def profile_page(request,user_id):
    context = {}


    user = User.objects.get(id = user_id)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username

        favorite_products = ProductUser.objects.filter(user_info_id=user)
        # Extract the product IDs from favorite_products
        product_ids = [fav_prod.product_info_id for fav_prod in favorite_products]

        # Query the products using the product IDs
        favorite_products_details = products.objects.filter(pk__in=product_ids)
        context['user'] =  user
        context['favorite_products'] = favorite_products_details
        return render(request, 'profile_page.html', context)    
    return render(request,'profile_page.html', context)
