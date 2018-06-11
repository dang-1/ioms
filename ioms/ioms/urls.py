"""ioms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from .views import IndexView, IndexView2

api_patterns = [
    path('users/', include('users.urls.api_urls'), name='api-users'),
    path('hostmanage/', include('hostmanage.urls.api_urls'), name='api-hostmanage'),
    path('site/', include('sitecollect.urls.api_urls'), name='api-sitecollect'),
    path('cmdb/', include('cmdb.urls.api_urls'), name='api-cmdb'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    #index page
    path('', IndexView.as_view(), name='index'),
    path('iomp', IndexView2.as_view(), name='iomp_index'),
    # general view
    path('users/', include('users.urls.view_urls'), name='users'),
    path('hostmanage/', include('hostmanage.urls.view_urls'), name='hostmanage'),
    path('sitecollect/', include('sitecollect.urls.view_urls'), name='sitecollect'),
    path('cmdb/', include('cmdb.urls.view_urls'), name='cmdb'),
    path('blog/', include('blog.urls'), name='blog'),
    #api url view map
    path('api2/', include(api_patterns)),
]
