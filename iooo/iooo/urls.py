"""iooo URL Configuration

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
from django.urls import path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required(login_url='/users/login')
# def IndexView(request):
#     # if request.user.is_authenticated:
#     #     print('auth ok')
#     # else:
#     #     print("auth fail")
#     title_name = 'index'
#     template_name = 'index2.html'
#
#     # def get(request):
#     #     pass
#     return render(request, template_name)

# class IndexView(TemplateView):
class IndexView(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     return super(IndexView, self).get(request, *args, **kwargs, )
    #
    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context['title_name'] = 'iomp: index page'
    #     return context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]
