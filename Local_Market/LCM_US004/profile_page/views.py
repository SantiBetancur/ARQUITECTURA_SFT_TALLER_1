from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user
from django.db.models import Q
from community_main_page.models import products,ProductUser
from django.contrib.auth.models import User
from Sellerprofile.models import Seller
from django.core.paginator import Paginator
from .forms import UserForm


# Create your views here.

def profile_page(request,user_id):
    context = {}

    user = User.objects.get(id = user_id)
    if user.is_authenticated:
     
        user_instance = User.objects.get(id = user.id)
        context['user'] = user
        is_seller = Seller.objects.filter(user_info = user_instance).exists()
        context['is_seller'] = is_seller
    if is_seller:
            seller_query = Seller.objects.filter(user_info = user_instance)
           
            for seller_instance in seller_query:
                if seller_instance.user_info.id == user_id:
                    context['seller_id'] = seller_instance.id
                    context['seller'] = seller_instance
                    break

    favorite_products = ProductUser.objects.filter(user_info_id=user)
    # Extract the product IDs from favorite_products
    product_ids = [fav_prod.product_info_id for fav_prod in favorite_products]

    # Query the products using the product IDs
    favorite_products_details = products.objects.filter(pk__in=product_ids)
    queryset_paginator =   Paginator(favorite_products_details, 3)
    page_number = request.GET.get('page')
    page_obj = queryset_paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['user'] =  user
    return render(request, 'profile_page.html', context)    

def profile_edit(request, user_id):
    try:
        context = {}
        user = get_user(request)
        U_User = User.objects.get(id = user_id)
        form = UserForm(initial={'username' : U_User.username, 'email' : U_User.email})
        is_seller = Seller.objects.filter(user_info = user).exists()

        if user.is_authenticated:
            context['session_user'] = user.username

        if request.method == 'POST':
            if 'delete' in request.POST:
                if is_seller:
                    context['form'] = form
                    context['form_error'] = "No puedes eliminar tu cuenta si te encuentras registrado como vendedor"
                    return render(request, 'profile_edit.html', context)

                else:
                    U_User.delete()
                    return redirect(f'/logout/')
        
           
                
            if request.POST['password'] == request.POST['password_confirmation']:

                if request.POST['username'] != U_User.username:

                
                    if User.objects.filter(username=request.POST['username']).exists():

                        context['form'] = form
                        context['form_error'] = "El usuario ingresado no está disponible"
                        return render(request, 'profile_edit.html', context)
                    else:

                        U_User.username = request.POST['username']
                        U_User.email = request.POST['email']
                        if request.POST['password']:
                            U_User.password = request.POST['password']
                        U_User.save()
                        return redirect(f'/available_communities/profile/{U_User.id}')
                
                else:

    
                    U_User.email = request.POST['email']
                    if request.POST['password']:
                            U_User.password = request.POST['password']
                    U_User.save()
                    return redirect(f'/available_communities/profile/{U_User.id}')
            else:
                context['form'] = form
                context['form_error'] = "La confirmación de la contraseña no coincide"
                return render(request, 'profile_edit.html', context)
         


        context['form'] = form
        return render(request, 'profile_edit.html', context)
    except User.DoesNotExist:
        return redirect(f'/')    
 
