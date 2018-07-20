#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午5:39
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.contrib import admin
from django.urls import path

from ..views import SiteTypeDetailView, SiteTypeListView, SiteTypeAddView, SiteTypeUpdateView, SiteTypeModelDeleteView, \
    SiteListView, SiteManageView, SiteDetailView, SiteAddView, SiteUpdateView, SiteDeleteView, \
    SiteTypeApiView
# from rest_framework import routers
#SiteIndex, SiteAddView, , ,

app_name = 'sitecollect'
# router = routers.DefaultRouter()
# router.register(r'site_type/list/api/', SiteTypeSerializer)

urlpatterns = [
    path('site_type/list/api/', SiteTypeApiView.as_view(), name='api-user'),
    path('site_type/list/', SiteTypeListView.as_view(), name='site_type_list'),
    path('site_type/add/', SiteTypeAddView.as_view(), name='site_type_add'),
    path('site_type/<int:pk>/detail/', SiteTypeDetailView.as_view(), name='site_type_detail'),
    path('site_type/<int:pk>/update/', SiteTypeUpdateView.as_view(), name='site_type_update'),
    path('site_type/<int:pk>/delete/', SiteTypeModelDeleteView.as_view(), name='site_type_delete'),

    path('site/list/', SiteListView.as_view(), name='site_list'),
    path('site/list/manage/', SiteManageView.as_view(), name='site_manage'),
    path('site/add/', SiteAddView.as_view(), name='site_add'),
    path('site/<int:pk>/', SiteDetailView.as_view(), name='site_detail'),
    path('site/<int:pk>/update/', SiteUpdateView.as_view(), name='site_update'),
    path('site/<int:pk>/delete/', SiteDeleteView.as_view(), name='site_delete'),
]