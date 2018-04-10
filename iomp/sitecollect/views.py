from django.shortcuts import render
from django.http import JsonResponse
#import json
#from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.

class SiteIndex(LoginRequiredMixin, ListView):
    template_name = 'sitecollect/index.html'
    context_object_name = 'site_list'
    model = SiteCollect

    def get_context_data(self, **kwargs):
        context = super(SiteIndex, self).get_context_data(**kwargs)
        context['title_name'] = 'url page'
        site_info = {}
        for k in SiteCollect.objects.all():
            if k.siteurl and k.sitename:
                try:
                    site_info[k.typeid.typename].update({k.sitename: k.siteurl})
                except:
                    site_info[k.typeid.typename] = {k.sitename: k.siteurl}
        context['site_info'] =  site_info
        return context


# def siteindex(request):
#     print(request.method)
#     site_info = {}
#
#     for k in SiteCollect.objects.all():
#         if k.siteurl and k.sitename:
#             try:
#                 site_info[k.typeid.typename].update({k.sitename: k.siteurl})
#             except:
#                 site_info[k.typeid.typename] = {k.sitename: k.siteurl}
#     return render(request, 'sitecollect/index.html', {'site_info': site_info})
#
# class siteindex2(TemplateView):
#     template_name = 'sitecollect/index.html'
#
#     def get(self, *args, **kwargs):
#         site_info = {}
#
#         for k in SiteCollect.objects.all():
#             if k.siteurl and k.sitename:
#                 try:
#                     site_info[k.typeid.typename].update({k.sitename: k.siteurl})
#                 except:
#                     site_info[k.typeid.typename] = {k.sitename: k.siteurl}
#         return site_info


# def site_index_api(request):
#     site_info = {}
#     for k in SiteCollect.objects.all():
#         if k.siteurl and k.sitename:
#             try:
#                 site_info[k.typeid.typename].update({k.sitename: k.siteurl})
#             except:
#                 site_info[k.typeid.typename] = {k.sitename: k.siteurl}
#     #return HttpResponse(site_info, mimetype='application/json')
#     return JsonResponse(site_info)
#
# def managesite(request):
#     return render(request, 'sitecollect/manage_site.html')

class SiteType(LoginRequiredMixin, ListView):
    template_name = 'sitecollect/site_type.html'
    context_object_name = 'site_type'
    model = SiteType

    def get_context_data(self, **kwargs):
        context = super(SiteType, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: url type page'
        return context

# def sitetypemanage(request):
#     type_info = {}
#     for i in SiteType.objects.all():
#         type_info[i.typename] = i.typeid
#
#     return render(request, 'sitecollect/site_type_manage.html', {'site_type_list': type_info})
#
# def addsite(request):
#     return render(request, 'sitecollect/add_site.html')
#
#
# def deletesite(request):
#     return render(request, 'sitecollect/delete_site.html')

