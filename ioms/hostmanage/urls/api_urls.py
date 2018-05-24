#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 下午4:47
# @Author  : tang
# @FileName: api_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django.conf.urls import url, include
from rest_framework import routers
from .. import api


router = routers.DefaultRouter()
router.register(r'host-list', api.HostListView)
router.register(r'host', api.HostView)
router.register(r'role', api.RoleView)
# routers.reverse(r'index', api.HostView)


# urlpatterns = router.urls

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'host/', api.HostView.as_view(), name='index'),
    # url(r'host/<int:pk>/', api.HostDetailView.as_view(), name='index'), #get put destory

]
