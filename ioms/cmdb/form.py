#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 下午1:26
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django import forms
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


