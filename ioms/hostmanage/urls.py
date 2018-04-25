#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:33
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com


# from django.conf.urls import url

# from .views import *

# app_name = 'hostmanage'

# urlpatterns = [
#     url(r'^host_index/$', HostIndex.as_view(), name='host_index'),
#     url(r'^host_detail/(?P<pk>[0-9]+)/$', HostDetailView.as_view(), name='host_detail'),
#     url(r'^host_detail/project_list/$', ProjectListView.as_view(), name='project_list'),
#     url(r'^host_detail/cloudplat_list/$', CloudPlatView.as_view(), name='cloudplat_list'),
#     url(r'^host_detail/role_list/$', RoleView.as_view(), name='role_list'),
#     #url(r'^host_add', host_add, name='host_add'),
# ]
from django.contrib import admin
from django.urls import path

from .views import HostIndexView, StatusView

app_name = 'hostmanage'

urlpatterns = [
    path('host_index/', HostIndexView.as_view(), name="host_index"),
    path('status_list/', StatusView.as_view(), name='status_list'),
    # path('site_index/', SiteIndex.as_view(), name='site_index'),
    # path('site_add/', SiteAddView.as_view(), name='site_add'),
    # path('site_type_index/', SiteType.as_view(), name='site_type_index'),
    # path('site_type_add/', SiteTypeAddView.as_view(), name='site_type_add'),
    # path('logout/', user_logout, name='logout'),
    # path('register/', Login.as_view(), name='register'),
    # # path('user_list/', Login.as_view(), name='user_list'),
    # path('useradd/', UserAdd.as_view(), name='useradd'),
    # path('user_list/', UserList.as_view(), name='user_list'),

]