"""Battle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Battle import settings
from django.contrib import admin
from django.urls import path,include
from .views import header,home
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('header',header,name='header'),
    path('',home,name='home'),

    path('information/',include('My_Information.urls',namespace='My_Information')),
    path('skills/',include('Skills.urls',namespace='Skills')),
    path('your-comments/',include('Your_Comments.urls',namespace='Your_Comments')),
    
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)