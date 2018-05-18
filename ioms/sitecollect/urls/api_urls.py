#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午4:54
# @Author  : tang
# @FileName: api_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com


from rest_framework import viewsets

# from .. import  api
from ..api import SiteTypeListView




# from django.conf.urls import url, include
from rest_framework import routers
# from .. import api
#
router = routers.DefaultRouter()
router.register(r'site_type', SiteTypeListView)
# # router.register(r'users2', api.UserViewSet2.as_view())
#
#
urlpatterns = router.urls