from django.shortcuts import render, HttpResponseRedirect
from publish_product.forms import ProductForm
from community_main_page.models import products
# Create your views here.

def publish(request):
    context = {}
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/EAFIT/home/')   
    
    context['form'] = form
    return render(request, "publish_product.html", context)
 
            
