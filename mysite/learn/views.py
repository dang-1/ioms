from django.shortcuts import render

# Create your views here.


def index(request):
    try:
        a = request.GET('a')
        b = request.GET('b')
    except:
        a,b  = 1,3
    return render(request, 'learn/index.html')

