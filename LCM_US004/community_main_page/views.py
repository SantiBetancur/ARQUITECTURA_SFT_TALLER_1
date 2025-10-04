from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from .models import ProductUser
# I am use the Q class to realize the request of the search
from django.db.models import Q
from django.contrib.auth import logout, get_user
from Sellerprofile.models import Seller
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.paginator import Paginator
from django.views.generic import TemplateView


# Create your views here.
'''
New view function for home page
'''
class HomeView(TemplateView):
    template_name = 'home.html'
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        
        # Get the search query
        search_query = request.GET.get("search")
        products_queryset = Product.objects.all()
        
        if search_query:
            products_queryset = products_queryset.filter(
                Q(name__icontains=search_query) |
                Q(price__icontains=search_query)
            )
        
        # Pagination
        paginator = Paginator(products_queryset, self.paginate_by)
        page_number = request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        
        # Authenticated user
        user = request.user  
        
        if user.is_authenticated:
            context['session_user'] = user.username
              
            try:
                seller = Seller.objects.select_related('user_info').get(user_info=user)
                context['is_seller'] = True
                context['seller_id'] = seller.id
                context['seller_name'] = seller.name
            except Seller.DoesNotExist:
                context['is_seller'] = False
        
        return context

'''
Old view function for home page
def home(request):
    context = {}

    products_queryset = Product.objects.all()
    search_query = request.GET.get("search")

    #Search by product attrs
    if search_query:
       
            # Si el valor de búsqueda no es un número, busca coincidencias parciales en los campos 'name' y 'description'
            products_queryset = Product.objects.filter(
                Q(name__icontains=search_query) |
                Q(price__icontains=search_query)
            )

   
    #Pagination of the products queryset
    queryset_paginator =   Paginator(products_queryset, 9)
    page_number = request.GET.get('page')
    page_obj = queryset_paginator.get_page(page_number)
    context['page_obj'] = page_obj

    user = get_user(request)
    user_instance = None
    seller_instance = None
    if user.is_authenticated:
        user_instance = User.objects.get(id = user.id)
        context['session_user'] = user_instance.username
        is_seller = Seller.objects.filter(user_info = user_instance).exists()
        context['is_seller'] = is_seller
        
        if is_seller:
            seller_instance = Seller.objects.filter(user_info = user_instance).first()
            context['seller_id'] = seller_instance.id
            context['seller_name'] = seller_instance.name
    return render(request, "home.html", context)
'''	
'''
New view function for product detail
'''
class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        product_id = kwargs['product_id']
        product = get_object_or_404(Product, pk=product_id)
        context['dataset'] = product
        
        user = request.user
        if user.is_authenticated:
            user_instance = User.objects.get(id=user.id)
            context['session_user'] = user_instance.username
            
            # Verificar si el producto ya está en favoritos
            existing_fav = ProductUser.objects.filter(
                user_info_id=user_instance, 
                product_info_id=product_id
            ).annotate(count=Count('id'))
            context['has_duplicates'] = len(existing_fav) > 0
            context['seller_id'] = product.seller_info.id
        
        return context
    
    def post(self, request, *args, **kwargs):
        """Maneja la adición/eliminación de productos a favoritos"""
        context = self.get_context_data(**kwargs)
        product_id = kwargs['product_id']
        user = request.user
        
        if not user.is_authenticated:
            return self.render_to_response(context)
        
        user_instance = User.objects.get(id=user.id)
        product = get_object_or_404(Product, pk=product_id)
        
        # Verificar si ya está en favoritos
        existing_fav = ProductUser.objects.filter(
            user_info_id=user_instance, 
            product_info_id=product_id
        )
        
        if existing_fav.exists():
            # Eliminar de favoritos
            existing_fav.delete()
            context['has_duplicates'] = False
        else:
            # Agregar a favoritos
            new_favorite = ProductUser()
            new_favorite.user_info = user_instance
            new_favorite.product_info = product
            new_favorite.save()
            context['has_duplicates'] = True
        
        # Actualizar contexto
        context['session_user'] = user_instance.username
        context['seller_id'] = product.seller_info.id
        
        return self.render_to_response(context)

'''
Old view function for product detail

def prod_detail(request, product_id):
        product = get_object_or_404(Product, pk = product_id)
        context = {}
        context['dataset'] = product
        user = get_user(request)

        user_instance = None
        has_duplicates = False
        if user.is_authenticated:
            user_instance = User.objects.get(id = user.id)
            context['session_user'] = user_instance.username
            existing_fav = ProductUser.objects.filter(user_info_id = user_instance, product_info_id = product_id).annotate(count=Count('id'))
            has_duplicates = len(existing_fav) > 0
            
            
            if request.method == 'POST':
                new_instance = ProductUser()
                user = User.objects.get(id = user.id)
                new_instance.user_info = user
                current_product = Product.objects.get(pk = product_id)
                if not has_duplicates: 
                    new_instance.product_info = current_product
                    new_instance.save()
                    has_duplicates = True
                    context['has_duplicates'] = has_duplicates
                    context['seller_id'] = product.seller_info.id
                    return render(request, 'product_detail.html', context)
                elif has_duplicates:
                    favorite = ProductUser.objects.filter(product_info = current_product)
                    favorite.delete()
                    has_duplicates = False
                    context['has_duplicates'] = has_duplicates
                    context['seller_id'] = product.seller_info.id
                    return render(request, 'product_detail.html', context)
            
                  
            context['seller_id'] = product.seller_info.id
            context['has_duplicates'] = has_duplicates
            return render(request, 'product_detail.html', context)
'''         
            

def user_logout(request):
    logout(request)
    return redirect('/')