from django.shortcuts import render, HttpResponseRedirect
from register_page.forms import UserForm
from register_page.models import User

# Create your views here.

def register(request):

    context = {}
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/EAFIT/home/')

    context['form'] = form
    return render(request, "register_page.html", context)