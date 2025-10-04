from django.shortcuts import render, redirect
from publish_product.forms import ProductForm, Image_prompt_form
from django.contrib.auth import logout, get_user
from django.contrib.auth.models import User
from openai import OpenAI
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from community_main_page.models import Product
from django.core.files import File
from Sellerprofile.models import Seller
from communityPage.models import Community
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



def publish(request, seller_id):
    
    context = {}
    form = ProductForm() 
    user = get_user(request)
    seller_instance = Seller.objects.get(id = seller_id)

    if user.is_authenticated:    
        context['username'] = user.username
        context['current_user_id'] = user.id
        
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.seller_info = seller_instance
            reg.save()
            return redirect(f'/available_communities/seller/{seller_instance.id}')  
        context["message"] = "Debes llenar los campos obligatorios" 
        context['form'] = form
        return render(request, "publish_product.html", context)

    context['form'] = form
    return render(request, "publish_product.html", context)

    


#This is the view of the image generation templates. 

def product_image_generation(request, seller_id):
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
            if user_prompt:
                context['prompt'] = user_prompt

                # Generate the image URL using the OpenAI API
                image_url = generate_image(user_prompt)
                if image_url == 1:
                    context['error'] = "This option is not available at the moment"
                    return render(request, 'get_user_prompt_temp.html', context) 

                # Fetch and save the image locally
                try:
                    save_path = "ia_images/image.jpg"  # Adjust based on your needs
                    saved_image_url = fetch_and_save_image(image_url, save_path)
                    context['image_url'] = saved_image_url
                    # If you want to show the image in your template, you can pass the saved_image_url to the context

                    #Set the image to the product

                except Exception as e:
                    context['error'] = str(e)

            return redirect(f'/available_communities/seller/{seller_id}/new_product/image_generation/preview/?image_url={saved_image_url}&user_prompt={user_prompt}')
    
    context['form'] = form
    return render(request, 'get_user_prompt_temp.html', context) 


def set_image_generated_to_product(request, seller_id):
    saved_image_url = request.GET.get('image_url')
    user_prompt = request.GET.get('user_prompt')
    context = {}
    user = get_user(request)
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username 
    
    if request.method == 'POST':
       
        return redirect(f'/available_communities/seller/{seller_id}/new_product/image_generation/finish/?image_url={saved_image_url}')
        


    context['image_url'] = saved_image_url
    context['prompt'] = user_prompt
    return render(request, 'image_generated_temp.html', context)


def finish_product_form(request, seller_id):
    context = {}
    form = ProductForm
    saved_image_url = request.GET.get('image_url')
   
    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
           
         
            with open('.'+saved_image_url   , 'rb') as image_file:
                print(type(image_file))
                django_file = File(image_file)
                product = Product.objects.create(image=django_file)
                form.instance = product
          
            form.save()
            return redirect(f'/available_communities/seller/{seller_id}/')  
        else:
            context["message"] = "Debes llenar los campos obligatorios" 
            context['form'] = form
            return render(request, "publish_product_finish.html", context)
        
    context['form'] = form
    user = get_user(request)
    current_user = ""
    if user.is_authenticated:
        current_user = user
        context['session_user'] = current_user.username   
    return render(request, "publish_product_finish.html", context)

    


def user_logout(request):
    logout(request)
    return redirect('/')

OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)
            
def generate_image(prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        return 1
