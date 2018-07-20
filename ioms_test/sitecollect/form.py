#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 上午11:01
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django import forms
from .models import SiteTypeModel, SiteCollectModel


class SiteForm(forms.ModelForm):
    class Meta:
        model = SiteCollectModel
        fields = '__all__'


# class SiteTypeAddForm(forms.ModelForm):
#     class Meta:
#         model = SiteType
#         fields = '__all__'

#
class SiteTypeForm(forms.ModelForm):
    class Meta:
        model = SiteTypeModel
        fields = ['site_type_name']


# class ConfirmDeleteForm(forms.ModelForm):


# class UserAddForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password_raw']
#
#         def clean_password(self):
#             password = cleaned_data.get('password')



