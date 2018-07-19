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

#dbtype
from ..views import DbTypeListView, DbTypeDetailView, DbTypeAddView, DbTypeUpdateView, DbTypeDeleteView
#master
from ..views import MasterDbListView, MasterDbAddView, MasterDbUpdateView
#slave
from ..views import SlaveDbListView, SlaveDbAddView, SlaveDbUpdateView

app_name = 'db'


urlpatterns = [
    path('db-type/list/', DbTypeListView.as_view(), name='db-type-list'),
    path('db_type/add/', DbTypeAddView.as_view(), name='db-type-add'),
    path('db_type/<int:pk>/', DbTypeDetailView.as_view(), name='db-type-detail'),
    path('db_type/<int:pk>/update/', DbTypeUpdateView.as_view(), name='db-type-update'),
    path('db_type/<int:pk>/delete/', DbTypeDeleteView.as_view(), name='db-type-delete'),

    path('db-list/', DbListView.as_view(), name='db-list'),

    path('master-db/list/', MasterDbListView.as_view(), name='master-db-list'),
    path('master-db/add/', MasterDbAddView.as_view(), name='master-db-add'),
    path('master-db/<int:pk>/update', MasterDbUpdateView.as_view(), name='master-db-update'),

    path('slave-db/list/', SlaveDbListView.as_view(), name='slave-db-list'),
    path('slave-db/add/', SlaveDbAddView.as_view(), name='slave-db-add'),
    path('slave-db/<int:pk>/update/', SlaveDbUpdateView.as_view(), name='slave-db-update'),
]