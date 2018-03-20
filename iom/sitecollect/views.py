from django.shortcuts import render

from .models import *
# Create your views here.

def siteindex(request):
    site_info = {}
    type_info = {}
    #eg: {'typeid':{a: b}, 'typeid':{a: b, c:d}}

    #get type name
    for i in SiteType.objects.all():
        site_info[i.typename] = {}
        type_info[i.typeid] = i.typename



    #get site
    all_site = SiteCollect.objects.all()
    for i in all_site:
        site_one = {i.sitename: i.siteurl}
        site_type = i.typeid

        site_info[type_info[site_type]].update(site_one)

    #return
    return render(request, 'sitecollect/index.html', {'site_info': site_info})


def addsite(request):
    return render(request, 'sitecollect/addsite.html')


def deletesite(request):
    return render(request, 'sitecollect/deletesite.html')

