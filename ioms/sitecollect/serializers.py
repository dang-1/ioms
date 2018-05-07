#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 下午3:28
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import serializers
from .models import SiteTypeModel

class SiteTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    site_type_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # class Meta:
    #     model = SiteTypeModel
    #     fields = ('id', 'site_type_name')





