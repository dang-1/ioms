from django.shortcuts import render
from django.shortcuts import render_to_response

def IndexView(request):
    template_name = 'index.html'
    return render(request, template_name)


#def page_not_found(request):
#    return render_to_response('404.html')
