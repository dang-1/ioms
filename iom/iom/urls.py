"""iom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from django.conf.urls import handler404, handler500
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hostmanage/', include('hostmanage.urls')),
    url(r'^users/', include('users.urls'), name='users'),
    url(r'^$', IndexView, name='index'),
    url(r'^sitecollect/', include('sitecollect.urls'), name='sitecollect'),
    url(r'cmdb/', include('cmdb.urls'), name='cmdb'),
    # 将 auth 应用中的 urls 模块包含进来
    url(r'^users/', include('django.contrib.auth.urls')),
]

#handler404 = page_not_found
#handler500 = page_not_found
#handler301 = page_not_found
