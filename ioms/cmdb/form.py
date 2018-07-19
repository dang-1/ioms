#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 下午1:26
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django import forms
from .models import Tag, GsStatus, ZoneName

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class GsStatusForm(forms.ModelForm):
    class Meta:
        model = GsStatus
        fields = "__all__"


class ZoneNameForm(forms.ModelForm):
    class Meta:
        model = ZoneName
        fields = "__all__"
