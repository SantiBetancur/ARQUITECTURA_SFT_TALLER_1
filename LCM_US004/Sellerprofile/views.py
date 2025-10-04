from django.shortcuts import render, redirect, Http404
from .models import Seller
from .forms import SellerForm
from django.contrib.auth import logout, get_user
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from publish_product.forms import ProductForm
from community_main_page.models import Product





def seller_info(request, seller_id):
    context = {}
    user = get_user(request)
    
    try:
        if Seller.objects.filter(pk =seller_id).exists():
            seller = Seller.objects.get(pk=seller_id)
            context['seller'] = seller
            context['seller_id'] = seller.id
            

            if user.is_authenticated:
                context['session_user'] = user.username

            context['page_text'] = "Administra tu perfil"
            context['current_user_id'] = user.id
            return render(request, 'seller.html', context)
        
        return redirect(f'/available_communities/profile/{user.id}')
    
    except Seller.DoesNotExist:
        return redirect(f'/available_communities/profile/{user.id}')

def seller_products(request, seller_id):
    context = {}
    seller = Seller.objects.get(pk=seller_id)
    context['seller'] = seller
    context['seller_id'] = seller.id
    context['editing_seller'] = True
    user = get_user(request)

    seller_products = Product.objects.filter(seller_info = seller)
    queryset_paginator =   Paginator(seller_products, 3)
    page_number = request.GET.get('page')
    page_obj = queryset_paginator.get_page(page_number)
    context['page_obj'] = page_obj
    

    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username

    if request.method == 'POST':

        if "edit" in request.POST:
               
                btn_value = request.POST['edit'] 
                return redirect(f'/available_communities/seller/products/{seller_id}/edit/{btn_value}')
        exist_product = Product.objects.filter(pk = request.POST['delete']).exists()        
        if "delete" in request.POST and exist_product:
            product = Product.objects.get(pk = request.POST['delete'])
            product.delete()
            

    context['page_text'] = "Estos son tus productos"
    context['current_user_id'] = current_user.id
    return render(request, 'seller_products.html', context)    


def product_edition(request, product_id, seller_id):
    context = {}
    current_user = ""
    user = get_user(request)
    context['page_text'] = "Edita el producto"
    context['editing_seller'] = True
    context['seller_id'] = seller_id
    product = Product.objects.get(pk = product_id)

    form = ProductForm(initial={'description': product.description, 'name': product.name, 'price':product.price})

    context['form'] = form

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if 'cancel' in request.POST:
            return redirect(f'/available_communities/seller/products/{seller_id}')
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()

            return redirect(f'/available_communities/seller/products/{seller_id}')
        
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username

    return render(request,'edit_product.html', context)

def seller_edition(request, seller_id):
    try:
            context = {}
            user = get_user(request)
            user_instance = None
            seller = Seller.objects.get(pk = seller_id)
            form = SellerForm(initial={'name': seller.name, 'email': seller.email, 'location': seller.location , 'phone':seller.phone, 'age':seller.age, 'description':seller.description})

            if user.is_authenticated:
                user_instance = User.objects.get(id=user.id)
                context['session_user'] = user_instance.username


            if request.method == 'POST':
                form = SellerForm(request.POST, request.FILES)
                if 'delete' in request.POST:

                    if Product.objects.filter(seller_info = seller).exists():
                        context['form_error'] = "Debes eliminar todos tus productos antes de eliminar tu cuenta"
                        context['form'] = form
                        context['editing_seller'] = True
                        context['seller_id'] = seller.id
                        context['page_text'] = "Edita tu perfil de vendedor"
                        return render(request, 'edit_seller.html', context)
                    
                    seller.delete()
                    return redirect(f'/available_communities/profile/{user.id}')

                if form.is_valid():
                    seller.name = form.cleaned_data['name']
                    seller.email = form.cleaned_data['email']
                    seller.location = form.cleaned_data['location']
                    seller.phone = form.cleaned_data['phone']
                    seller.age = form.cleaned_data['age']
                    seller.description = form.cleaned_data['description']
                    if 'photo' in request.FILES:
                        seller.photo = request.FILES['photo']
                    if 'permission' in request.FILES:
                        seller.permission = request.FILES['permission']
                    seller.save()
                    return redirect(f'/available_communities/seller/{seller_id}')        
                

                context['form'] = form
                context['seller_id'] = seller.id
                context['form_error'] = "Campos no válidos, intenta de nuevo."
                context['editing_seller'] = True
                context['page_text'] = "Edita tu perfil de vendedor"
                return render(request, 'edit_seller.html', context)
            
            context['form'] = form
            context['editing_seller'] = True
            context['page_text'] = "Edita tu perfil de vendedor"
            context['seller_id'] = seller.id
            return render(request, 'edit_seller.html', context)
    except Seller.DoesNotExist:
        return redirect(f'/available_communities/profile/{user.id}')    


def seller_registration(request):
    context = {}
    form = SellerForm()
    user = get_user(request)
    user_instance = None

    if user.is_authenticated:
        user_instance = User.objects.get(id=user.id)
        context['session_user'] = user_instance.username

    if request.method == 'GET':
        context['form'] = form
        return render(request, 'seller_register.html', context)

    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)

        if form.is_valid():
            # Verificar si el usuario ya está registrado como vendedor
            existing_seller = Seller.objects.filter(user_info=user_instance).exists()

            if not existing_seller:
                # Si el usuario no está registrado como vendedor, guardar el formulario
                reg = form.save(commit=False)
                reg.user_info = user_instance
                reg.active_seller = True
                reg.save()
                return redirect(f'/available_communities/seller/{reg.id}')
            else:
               
                context['form'] = form
                context['form_error'] = "Ya te encuentras registrado como vendedor"
                return render(request, 'seller_register.html', context)

        context['form'] = form
        context['form_error'] = "Campos no válidos, intenta de nuevo."
        return render(request, 'seller_register.html', context) 

    

def user_logout(request):
    logout(request)
    return redirect('/')