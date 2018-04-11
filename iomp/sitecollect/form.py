#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 上午11:01
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com




from django import forms
from .models import SiteType

class SiteTypeAddForm(forms.ModelForm):
    class Meta:
        model = SiteType
        fields = '__all__'





# class UserAddForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password_raw']
#
#         def clean_password(self):
#             password = cleaned_data.get('password')



