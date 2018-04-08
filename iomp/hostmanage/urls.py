#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:33
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com


from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^host_index', HostIndex.as_view(), name='host_index'),
    #url(r'^host_add', host_add, name='host_add'),
]

