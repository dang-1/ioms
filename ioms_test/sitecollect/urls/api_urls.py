#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午4:54
# @Author  : tang
# @FileName: api_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import routers
from ..api import SiteTypeListView, SiteListView
# from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'site/type', SiteTypeListView)
router.register(r'site', SiteListView)

urlpatterns = router.urls