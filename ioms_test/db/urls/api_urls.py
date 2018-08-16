#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 上午10:02
# @Author  : tang
# @FileName: api_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from rest_framework import routers
from .. import api

router = routers.DefaultRouter()
router.register(r'master', api.MasterDbView)
# router.register(r'db-list2', api.MasterDbView2)
router.register(r'slave', api.SlaveDbAPI)

urlpatterns = router.urls


