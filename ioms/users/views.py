#coding: utf-8
from django.shortcuts import render

from .form import UserForm, LoginForm,UserAddForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User

__all__ = [
    'Login', 'user_logout', 'UserList', 'UserAdd', 'test_page'
]


class Login(TemplateView):
    template_name = 'users/login.html'


    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)  # 将数据绑定到表单
        if login_form.is_valid(): #验证
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(username, password)
            try:
                user = authenticate(username=username, password=password)
            except:
                return HttpResponseRedirect("/users/login/")
            if user is not None:
                print('exec auth')
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/users/login/")
        else:
            return HttpResponseRedirect("/users/login/")

#class Logout(TemplateView):

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/login')


# def register(request):
#     if request.method == "POST":
#         user_form = UserForm(request.POST) #将数据绑定到表单
#         if user_form.is_valid(): #验证
#             username = user_form.cleaned_data['username']
#             useremail = user_form.cleaned_data['email']
#             password = user_form.cleaned_data['password']
#             #print(username, password)
#             #if authenticate(username=username, password=password):
#             #    print('login ok')
#             #    return HttpResponseRedirect("/")
#     else:
#         form = LoginForm()
#
#         #print(type(login_form))
#         ##if login_form.is_valied:
#         #username = login_form.cleaned_data['username']
#         #password = login_form.cleaned_data['password']
#         #print('========={} {}'.format(username, password))
#     return render(request, 'users/register.html')


class UserList(LoginRequiredMixin, ListView):
    template_name = 'users/user_list.html'

    context_object_name = 'user_list'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['title_name'] = 'user list page'
        return context


class UserAdd(TemplateView):
    template_name = 'users/user_add.html'

    def get_context_data(self, **kwargs):
        context = super(UserAdd, self).get_context_data(**kwargs)
        context['title_name'] = 'user add page'
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.method)
        user_add_form = UserAddForm(request.POST)
        if user_add_form.is_valid():
            print('user add valid')
            user_name = user_add_form.cleaned_data['username']
            email = user_add_form.cleaned_data['email']
            password = user_add_form.cleaned_data['password']
            print(user_name, email, password)
            try:
                new_user = User(
                    name = user_name,
                    username = user_name,
                    email = email,
                )
                new_user.password_raw = password
                new_user.save()
                print('save success')
                # user_add_form.save()
            except Exception as e:
                print('add fail {}'.format((e)))
                return HttpResponseRedirect("/users/useradd/")
            finally:
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/users/useradd/")

def test_page(request):
    return render(request, 'users/test_page.html')