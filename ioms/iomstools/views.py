from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file', None)
        if upload_file is None:
            return HttpResponse('No file get')
        else:
            with open('/tmp/{}'.format(upload_file.name), 'wb') as f:
                f.write(upload_file.read())
            return HttpResponse('Ok')
    else:
        return render(request, 'blog/upload.html')

def download(request, file_name):
    f = open('/tmp/{}'.format(file_name), 'rb')
    response = HttpResponse(f, content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
    f.close()
    return response

