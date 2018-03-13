from django.shortcuts import render
from django.http import HttpResponse
from hostnamage.models import *
# Create your views here.



def host_index(request):
    posts = models.Host.objects.all()
    return render(request, 'hostmanage/index.html', posts)




