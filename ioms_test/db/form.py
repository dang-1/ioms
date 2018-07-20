#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 下午3:40
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django import forms
from .models import DbType, MasterDb, SlaveDb

class DbTypeForm(forms.ModelForm):
    class Meta:
        model = DbType
        fields = "__all__"


class MasterDbForm(forms.ModelForm):
    class Meta:
        model = MasterDb
        fields = "__all__"
        # fields = ('type', 'alias', 'alias', 'db_port', 'status', 'open_time')


class SlaveDbForm(forms.ModelForm):
    class Meta:
        model = SlaveDb
        fields = "__all__"
        # fields = ('type', 'alias', 'alias', 'db_port', 'status', 'open_time')
