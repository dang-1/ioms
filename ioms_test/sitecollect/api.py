#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午4:33
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from rest_framework import generics, viewsets

from .serializers import SiteTypeSerializers, SiteSerializers
from .models import SiteTypeModel, SiteCollectModel


# from rest_framework.permissions import Is


#================================site type begin==============================================


class SiteTypeListView(viewsets.ModelViewSet):
    queryset = SiteTypeModel.objects.all()
    serializer_class = SiteTypeSerializers



#================================site type end==============================================

#================================site begin==============================================
class SiteListView(viewsets.ModelViewSet):
    queryset = SiteCollectModel.objects.all()
    serializer_class = SiteSerializers



#================================site end==============================================