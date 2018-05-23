#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午4:23
# @Author  : tang
# @FileName: api_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com



from django.conf.urls import url, include
from rest_framework import routers
from .. import api

router = routers.DefaultRouter()
router.register(r'gs-list', api.ConfigManageView)
# router.register(r'users', api.UserViewSet)
# # router.register(r'users2', api.UserViewSet2.as_view())

#
urlpatterns = router.urls

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]