from django.shortcuts import render
from django.http import HttpResponse
from hostmanage.models import *
# Create your views here.



def host_index(request):
    posts = Host.objects.all()
    return render(request, 'hostmanage/index.html', {'posts':posts})

def host_add(request):
    return render(request, 'hostmanage/host_add.html')


