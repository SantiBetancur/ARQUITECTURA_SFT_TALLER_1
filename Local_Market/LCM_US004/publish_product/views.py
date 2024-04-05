from django.shortcuts import render, redirect
from publish_product.forms import ProductForm, Image_prompt_form
from django.contrib.auth import logout, get_user
# Create your views here.

def publish(request):
    context = {}
    form = ProductForm() 
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/available_communities/EAFIT/products/')  
        context["message"] = "Debes llenar los campos obligatorios" 
        context['form'] = form
        return render(request, "publish_product.html", context)
    context['form'] = form

    user = get_user(request)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username   
    return render(request, "publish_product.html", context)


#This is the view of the image generation templates. 
def product_image_generation(request):
    context = {}
    form = Image_prompt_form()
    user = get_user(request)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username 
    if request.method == 'POST':

        #Send this prompt to the OpenIA API to generate the image
        user_prompt = request.POST['user_image_prompt']
        context['prompt'] = user_prompt

        #If the user accept the generated image, save it in 'images_generated' model, then redirect the user to the publish product form
        
        return render(request, 'image_generated_temp.html', context)
    
    context['form'] =form
    return render(request, 'get_user_prompt_temp.html', context)
    


def user_logout(request):
    logout(request)
    return redirect('/')
 
            
