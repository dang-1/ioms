#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午4:33
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from .serializers import SiteTypeSerializers
from .models import SiteTypeModel, SiteCollectModel

from rest_framework import generics
# from rest_framework.permissions import Is


class SiteTypeList(generics.ListCreateAPIView):
    queryset = SiteTypeModel.objects.all()
    serializer_class = SiteTypeSerializers










