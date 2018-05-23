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

from .serializers import ConfigMangeSerializer
from .models import ConfigManage

class ConfigManageView(viewsets.ModelViewSet):
    queryset = ConfigManage.objects.all().order_by('id')
    serializer_class = ConfigMangeSerializer
    # pass

