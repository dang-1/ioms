#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午1:58
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django import forms
from .models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']


class UserAddForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

# class UserAddForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password_raw']
#
#         def clean_password(self):
#             password = cleaned_data.get('password')
     