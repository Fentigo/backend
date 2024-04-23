"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from portfolio import views


router = routers.DefaultRouter()
router.register(r'bookings', views.BookingsView, 'bookings'),
router.register(r'images', views.ImageView, 'image'),
router.register(r'videos', views.VideoView, 'videos'),
router.register(r'poet', views.PoetView, 'poet' ),
router.register (r'socialmedia', views.SocialMediaView, 'socialmedia'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path( 'api/poet/<int:poet_id>/description/', views.get_poet_description, name='get_poet_description'),
    path('api/socialmedia/<int:social_media_id>/url/', views.get_social_media_id, name='get_social_media_id'),
    path('api/image/<int:image_id>/image/', views.get_image_file, name='get_image_file'),


    
   ]
