from django.shortcuts import render, redirect
from publish_product.forms import ProductForm, Image_prompt_form
from django.contrib.auth import logout, get_user
from openai import OpenAI
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
# Create your views here.

def fetch_and_save_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        # Assuming save_path includes the filename. For example, 'images/my_image.jpg'.
        # You may need to adjust the path based on your MEDIA_ROOT settings.
        path = default_storage.save(save_path, ContentFile(response.content))
        return default_storage.url(path)
    else:
        raise Exception("Failed to fetch image from URL.")



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
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username 
    if request.method == 'POST':
        form = Image_prompt_form(request.POST)
        if form.is_valid():
            user_prompt = form.cleaned_data['user_image_prompt']
            context['prompt'] = user_prompt

            # Generate the image URL using the OpenAI API
            image_url = generate_image(user_prompt)

            # Fetch and save the image locally
            try:
                save_path = "path/to/save/image.jpg"  # Adjust based on your needs
                saved_image_url = fetch_and_save_image(image_url, save_path)
                context['image_url'] = saved_image_url
                # If you want to show the image in your template, you can pass the saved_image_url to the context
            except Exception as e:
                context['error'] = str(e)

        return render(request, 'image_generated_temp.html', context)
    
    context['form'] = form
    return render(request, 'get_user_prompt_temp.html', context) 


def user_logout(request):
    logout(request)
    return redirect('/')

client = OpenAI()
            
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1,
    )
    return response.data[0].url
