#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 上午11:01
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django import forms

from .models import Host, HostRole, HostStatus, ProjectName, CloudPlat
class HostFrom(forms.ModelForm):
    class Meta:
        model = Host
        # fields = '__all__'
        fields = ['hostname', 'outer_ip', 'inner_ip', 'role', 'project', 'instance_id']


class HostRoleForm(forms.ModelForm):
    class Meta:
        model = HostRole
        fields = ['role']


class PorjectFrom(forms.ModelForm):
    class Meta:
        model = ProjectName
        fields = ['project_name']


class CloudPlatForm(forms.ModelForm):
    class Meta:
        model = CloudPlat
        fields = ['cloud_platform_name']


class HostStatusForm(forms.ModelForm):
    class Meta:
        model = HostStatus
        fields = ['status']


# class SiteForm(forms.ModelForm):
#     class Meta:
#         model = SiteCollectModel
#         fields = '__all__'