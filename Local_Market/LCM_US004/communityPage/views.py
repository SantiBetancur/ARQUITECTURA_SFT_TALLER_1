from django.shortcuts import render
from communityPage.models import communities

# Create your views here.
def communityPage(request):
    community = communities.objects.all()    
    return render(request, "community_page.html", {"dataset": community})
