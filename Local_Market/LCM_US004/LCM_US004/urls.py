"""
URL configuration for LCM_US004 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from community_main_page import views as cm_v
from communityPage import views as cp_v
from publish_product import views as ps_v
from register_page import views as rp_v
from Login import views as lg_v
from profile_page import views as pp_v
from Sellerprofile import views as sp_v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('available_communities/EAFIT/products/', cm_v.home),
    path('available_communities/EAFIT/products/details/<int:product_id>', cm_v.prod_detail),
    path('available_communities/profile/details/<int:product_id>', cm_v.prod_detail),
    path('register/',rp_v.register),
    path('',cp_v.communityPage),
    path('available_communities/',cp_v.communityPage),
    path('logout/', cp_v.user_logout),
    path('available_communities/seller/<int:seller_id>/new_product/', ps_v.publish),
    path('available_communities/seller/<int:seller_id>/new_product/image_generation/', ps_v.product_image_generation),
    path('available_communities/seller/<int:seller_id>/new_product/image_generation/preview/', ps_v.set_image_generated_to_product),
    path('available_communities/seller/<int:seller_id>/new_product/image_generation/finish/', ps_v.finish_product_form),
    path('login/',lg_v.Login),
    path('available_communities/seller_registration/', sp_v.seller_registration),
    path('available_communities/seller/<int:seller_id>', sp_v.seller_info),
    path('available_communities/seller/products/<int:seller_id>', sp_v.seller_products),
    path('available_communities/seller/products/<int:seller_id>/edit/<int:product_id>', sp_v.product_edition),
     path('available_communities/seller/<int:seller_id>/edit_me/', sp_v.seller_edition),
    path('available_communities/profile/<int:user_id>', pp_v.profile_page)
    ]
   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
