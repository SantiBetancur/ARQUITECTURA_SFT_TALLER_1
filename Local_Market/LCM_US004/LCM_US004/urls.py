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
    path('', cp_v.communityPage),
    path('EAFIT/home/', cm_v.home),
    path('EAFIT/username/Profile/', ps_v.publish),
    path('home/register/', rp_v.register),
    path('home/seller/', sp_v.seller_info),
    path('EAFIT/register/', rp_v.register),
    path('EAFIT/Login/', lg_v.Login),
    path('available_communities/profile/', pp_v.profile_page),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
