#coding: utf-8
from django.shortcuts import render

from .form import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
#login
from django.contrib import auth

class Login(TemplateView):
    template_name = 'users/login.html'

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)  # 将数据绑定到表单
        if login_form.is_valid(): #验证
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #print(username, password)
            user = authenticate(username=username, password=password)
            #if authenticate(username=username, password=password):
            if user is not None:
                print('exec auth')
                login(request, user)
                return HttpResponseRedirect("/") #.set_cookie('username', username, 3600)

#class Logout(TemplateView):

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login')

# def login(request):
#     #form = LoginForm()
#     if request.method == "POST":
#         login_form = LoginForm(request.POST) #将数据绑定到表单
#         if login_form.is_valid(): #验证
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             print(username, password)
#             if authenticate(username=username, password=password):
#                 print('login ok')
#                 return HttpResponseRedirect("/")
#     else:
#         form = LoginForm()
#
#         #print(type(login_form))
#         ##if login_form.is_valied:
#         #username = login_form.cleaned_data['username']
#         #password = login_form.cleaned_data['password']
#         #print('========={} {}'.format(username, password))
#     return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST) #将数据绑定到表单
        if user_form.is_valid(): #验证
            username = user_form.cleaned_data['username']
            useremail = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            #print(username, password)
            #if authenticate(username=username, password=password):
            #    print('login ok')
            #    return HttpResponseRedirect("/")
    else:
        form = LoginForm()

        #print(type(login_form))
        ##if login_form.is_valied:
        #username = login_form.cleaned_data['username']
        #password = login_form.cleaned_data['password']
        #print('========={} {}'.format(username, password))
    return render(request, 'users/register.html')
