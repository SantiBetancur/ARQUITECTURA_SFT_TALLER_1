from django.shortcuts import render, redirect
from .models import Seller
from .forms import SellerForm
from django.contrib.auth import logout, get_user
from django.contrib.auth.models import User



def seller_info(request, seller_id):

    context = {}
    
    seller = Seller.objects.get(pk=seller_id)
    context['seller'] = seller
    user = get_user(request)
   
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username

    context['current_user_id'] = current_user.id
    return render(request, 'seller.html', context)



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
                # Si el usuario ya está registrado como vendedor, mostrar un mensaje de error
                context['form'] = form
                context['form_error'] = "Ya te encuentras registrado como vendedor"
                return render(request, 'seller_register.html', context)

        context['form'] = form
        context['form_error'] = "Campos no válidos, intenta de nuevo."
        return render(request, 'seller_register.html', context) 

    

def user_logout(request):
    logout(request)
    return redirect('/')