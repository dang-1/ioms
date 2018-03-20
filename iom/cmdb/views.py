#coding: utf-8
from django.shortcuts import render

from .models import *

# Create your views here.

def cmdb_index(request):
    all_conf = ConfigManage.objects.all()
    #for x in all_conf:
    #    print(x.gs_ip)
    return render(request, 'cmdb/index.html',{'all_conf': all_conf})


