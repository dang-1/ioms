#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午4:22
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets, routers

from .serializers import ConfigMangeSerializer #, GsConfigSerializer #, DbConfigSerializer
from .models import GsConfig #, DbConfig

class ConfigManageView(viewsets.ModelViewSet):
    queryset = GsConfig.objects.all().order_by('id')
    serializer_class = ConfigMangeSerializer
    depth = 1
    # pass

# class GsConfigManageView(viewsets.ModelViewSet):
#     queryset = GsConfig.objects.all().order_by('id')
#     serializer_class = GsConfigSerializer
#     depth = 1


# class DbConfigView(viewsets.ModelViewSet):
#     queryset = DbConfig.objects.all()
#     serializer_class = DbConfigSerializer
#     depth = 1

