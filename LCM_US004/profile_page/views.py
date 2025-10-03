from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from django.core.paginator import Paginator
from .forms import UserForm
from .containers import Container

container = Container()

def profile_page(request, user_id):
    user_repo = container.user_repo()
    seller_repo = container.seller_repo()
    product_repo = container.product_repo()

    user = user_repo.get_by_id(user_id)
    context = {}

    if not user:
        return redirect('/')

    if user.is_authenticated:
        context['user'] = user
        is_seller = seller_repo.is_seller(user)
        context['is_seller'] = is_seller

        if is_seller:
            seller_instance = seller_repo.get_by_user(user)
            if seller_instance:
                context['seller_id'] = seller_instance.id
                context['seller'] = seller_instance

    favorite_products_details = product_repo.get_favorites_by_user(user)
    queryset_paginator = Paginator(favorite_products_details, 3)
    page_number = request.GET.get('page')
    page_obj = queryset_paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'profile_page.html', context)


def profile_edit(request, user_id):
    user_repo = container.user_repo()
    seller_repo = container.seller_repo()

    try:
        context = {}
        user = get_user(request)
        U_User = user_repo.get_by_id(user_id)

        if not U_User:
            return redirect('/')

        form = UserForm(initial={'username': U_User.username, 'email': U_User.email})
        is_seller = seller_repo.is_seller(user)

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
                    return redirect('/logout/')

            if request.POST['password'] == request.POST['password_confirmation']:
                if request.POST['username'] != U_User.username:
                    if user_repo.exists_by_username(request.POST['username']):
                        context['form'] = form
                        context['form_error'] = "El usuario ingresado no está disponible"
                        return render(request, 'profile_edit.html', context)
                    else:
                        U_User.username = request.POST['username']
                        U_User.email = request.POST['email']
                        if request.POST['password']:
                            U_User.set_password(request.POST['password'])
                            U_User.save()
                            return redirect('/logout/')
                        else:
                            U_User.save()
                            return redirect('/logout/')
                else:
                    U_User.email = request.POST['email']
                    if request.POST['password']:
                        U_User.set_password(request.POST['password'])
                        U_User.save()
                        return redirect('/logout/')
                    else:
                        U_User.save()
                        return redirect('/logout/')
            else:
                context['form'] = form
                context['form_error'] = "La confirmación de la contraseña no coincide"
                return render(request, 'profile_edit.html', context)

        context['form'] = form
        return render(request, 'profile_edit.html', context)
    except Exception:
        return redirect('/')
