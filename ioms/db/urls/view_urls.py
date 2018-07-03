#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 下午2:22
# @Author  : tang
# @FileName: view_urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.urls import path
# from rest_framework import routers

from ..views import DbListView

app_name = 'db'


urlpatterns = [
    path('db-list/', DbListView.as_view(), name='db-list'),
    # path('db-detail/<int:pk>/', DbDetailView.as_view(), name='db-detail'),
    # path('gs-status/', GsStatusView.as_view(), name='gs-status'),
    # path('zone-name/', ZoneNameView.as_view(), name='zone-name'),
    # path('gs-list/', GsListView.as_view(), name='gs-list'),
    # path('db-list/', DbListView.as_view(), name='db-list'),
    # path('host_index/', HostIndexView.as_view(), name="host_index"),
    # path('status_list/', StatusView.as_view(), name='status_list'),
    # path('site_index/', SiteIndex.as_view(), name='site_index'),
    # path('site_add/', SiteAddView.as_view(), name='site_add'),
    # path('site_type_index/', SiteType.as_view(), name='site_type_index'),
    # path('site_type_add/', SiteTypeAddView.as_view(), name='site_type_add'),
]