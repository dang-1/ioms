#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午5:39
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.contrib import admin
from django.urls import path

from .views import SiteTypeDetailView, SiteTypeListView, SiteTypeAddView, SiteTypeUpdateView, SiteTypeModelDeleteView

#SiteIndex, SiteAddView, , ,

app_name = 'sitecollect'

urlpatterns = [
    path('site_type/list/', SiteTypeListView.as_view(), name='site_type_list'),
    path('site_type/add/', SiteTypeAddView.as_view(), name='site_type_add'),
    path('site_type/<int:pk>/', SiteTypeDetailView.as_view(), name='site_type_detail'),
    path('site_type/<int:pk>/update/', SiteTypeUpdateView.as_view(), name='site_type_update'),
    path('site_type/<int:pk>/delete/', SiteTypeModelDeleteView.as_view(), name='site_type_delete'),
    # path('site_index/', SiteIndex.as_view(), name='site_index'),
    # path('site_add/', SiteAddView.as_view(), name='site_add'),
    # path('site_type_index/', SiteType.as_view(), name='site_type_index'),
    # path('site_type_add/', SiteTypeAddView.as_view(), name='site_type_add'),
    # path('site_type/', SiteTypeView.as_view(), name='site_type'),

    # path('site_type/<int:pk>/', SiteTypeDetailView.as_view(), name='site_type_detail'),

]