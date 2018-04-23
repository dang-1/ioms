from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect,render_to_response
from django import forms
#from models import User
import hashlib
# Create your views here.

def usermanage_index(request):
    return render(request, 'usermanage/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username):
            return HttpResponse('<h1>用户已存在!</h1>')
        else:
            password = add_password(request.POST['password'])
            email = request.POST['email']
            phone = request.POST['phone']
            user = User.objects.create(
                username=username, password=password, email=email, phone=phone)
            request.session["username"] = user.username
            return redirect('/')

    return render(request, 'register.html', locals())


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = add_password(request.POST['password'])
        user_objs = User.objects.filter(username=username)
        if len(user_objs) == 1:
            user = user_objs[0]
            request.session["username"] = user.username
            return redirect('/')
        else:
            return HttpResponse('<h1>用户不存在或者密码账号输入不正确</h1>')
    else:
        return render(request, 'login.html', locals())
    return render(request, 'index.html', locals())


def logout_view(request):
    del request.session
    return render(request, 'index.html', locals())


def add_password(password):
    m = hashlib.md5(password).hexdigest()
    return m




