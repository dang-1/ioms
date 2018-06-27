#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:33
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.urls import path
# from rest_framework import routers

from ..views import GsStatusView, ZoneNameView, GsListView, \
    DbListView

app_name = 'cmdb'


urlpatterns = [
    path('gs-status/', GsStatusView.as_view(), name='gs-status'),
    path('zone-name/', ZoneNameView.as_view(), name='zone-name'),
    path('gs-list/', GsListView.as_view(), name='gs-list'),
    path('db-list/', DbListView.as_view(), name='db-list'),
    # path('host_index/', HostIndexView.as_view(), name="host_index"),
    # path('status_list/', StatusView.as_view(), name='status_list'),
    # path('site_index/', SiteIndex.as_view(), name='site_index'),
    # path('site_add/', SiteAddView.as_view(), name='site_add'),
    # path('site_type_index/', SiteType.as_view(), name='site_type_index'),
    # path('site_type_add/', SiteTypeAddView.as_view(), name='site_type_add'),
]