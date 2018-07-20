#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 下午1:26
# @Author  : tang
# @FileName: form.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django import forms
from .models import Tag, GsStatus, ZoneName, GsConfig

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


class GsConfigForm(forms.ModelForm):
    class Meta:
        model = GsConfig
        # fields = "__all__"
        fields = ('used', 'gs_ip', 'gs_zone', 'tag', 'gs_id', 'gs_alias', 'gs_accelerate_port', 'gs_dir',
                  'gs_name', 'gs_status', 'gs_open_time', 'gs_branch', 'gs_branch_commit_id',
                  'gs_merged', 'gs_merged_time', 'gs_merged_to_id',
                  'gs_db_name', 'gs_log_db_name', 'gs_db')