from django.shortcuts import render, redirect
from publish_product.forms import ProductForm
from django.contrib.auth import logout, get_user
# Create your views here.

def publish(request):
    context = {}
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/EAFIT/products/')  
        context["message"] = "Error" 
        return render(request, "publish_product.html", context)
    context['form'] = form

    user = get_user(request)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username
    return render(request, "publish_product.html", context)

def user_logout(request):
    logout(request)
    return redirect('/')
 
            
