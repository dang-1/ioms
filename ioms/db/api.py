#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 上午10:02
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import serializers, viewsets, routers

from .serializers import MasterDbSerializer, MasterDbSerializer2
from .models import MasterDb


class MasterDbView(viewsets.ModelViewSet):
    queryset = MasterDb.objects.all().order_by('id')
    serializer_class = MasterDbSerializer
    depth = 1


class MasterDbView2(viewsets.ModelViewSet):
    queryset = MasterDb.objects.all().order_by('id')
    serializer_class = MasterDbSerializer2
    depth = 1
# from .serializers import ConfigMangeSerializer, GsConfigSerializer, DbConfigSerializer
# from .models import GsConfig, DbConfig
#
# class ConfigManageView(viewsets.ModelViewSet):
#     queryset = GsConfig.objects.all().order_by('id')
#     serializer_class = ConfigMangeSerializer
#     depth = 1


