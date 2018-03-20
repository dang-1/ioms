from django.shortcuts import render


from django import forms
from models import User

# Create your views here.


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

#register
def regist(request):
    if request.method == 'POST':
        pass


