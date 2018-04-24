#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 上午11:01
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django import forms


class HostDetailFrom(forms.Form):
    host_id = forms.CharField(max_length=50, widget=forms.TextInput())
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput())

