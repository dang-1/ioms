#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 上午9:26
# @Author  : tang
# @FileName: api_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

# from django.urls import path
# from ..api import UserViewSet
# from django.conf.urls import url, include
# from rest_framework import routers
# # from tutorial.quickstart import views
app_name = 'users-api'
#
# # urlpatterns = [
# #     path(),
# # ]
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# urlpatterns = [
#     # path(r'', include(router.urls)),
#     # path(r'api/users/', include('rest_framework.urls', namespace='rest_framework')),
#     path('user/', UserViewSet.as_view(), name='user-api'),
# ]

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from django.urls import path
from .. import api

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'groups', api.GroupView, 'gropu')
# router.register(r'users2', api.UserViewSet2.as_view())
# router2 = BulkRouter()
# router2.register(r'user3', api.UserView)



# urlpatterns = [
#     # path('token/', api.UserToken.as_view(), name='user-token'),
# ]
urlpatterns = router.urls #+ router2.urls

