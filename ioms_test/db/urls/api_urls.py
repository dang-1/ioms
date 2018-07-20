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
router.register(r'db-list', api.MasterDbView)
router.register(r'db-list2', api.MasterDbView2)
# router.register(r'gs-list1', api.GsConfigManageView)
# router.register(r'db-list', api.DbConfigView)
# router.register(r'users', api.UserViewSet)
# # router.register(r'users2', api.UserViewSet2.as_view())

#
urlpatterns = router.urls


