from django.shortcuts import render
from django.contrib.auth import logout, get_user
from django.db.models import Q


# Create your views here.

def profile_page(request):
    context = {}



    user = get_user(request)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username
        return render(request, 'profile_page.html', context)    



    return render(request,'profile_page.html')
