#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 下午3:28
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import SiteCollectModel, SiteTypeModel



class SiteTypeSerializers(ModelSerializer):
    class Meta:
        model = SiteTypeModel
        # fields = ('id', 'site_type_name')
        fields = '__all__'


class SiteSerializers(ModelSerializer):
    class Meta:
        model = SiteCollectModel
        fields = '__all__'
        depth = 1







