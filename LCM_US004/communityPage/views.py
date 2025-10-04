from django.shortcuts import render, redirect
from communityPage.models import Community
from django.db.models import Q
from django.contrib.auth import logout, get_user
# Create your views here.

def communityPage(request):
    search_query = request.GET.get("search")
    communities_queryset = Community.objects.all()

    if search_query:
        communities_queryset = Community.objects.filter(
            Q(name__contains=search_query)
        )

    context = {
        'dataset': communities_queryset
    }


    user = get_user(request)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username
        return render(request, 'community_logged_page.html', context)

    return render(request, "community_page.html", context)

def user_logout(request):
    logout(request)
    return redirect('/')