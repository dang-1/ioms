#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:33
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.urls import path

from ..views import update_host_view,HostIndexView, HostStatusView, HostStatusDetailView, upload, \
    ProjectListView

#role
from ..views import HostRoleView, HostRoleAddView, HostRoleUpdateView, HostRoleDeleteView


app_name = 'hostmanage'

urlpatterns = [
    path('host/role/list/', HostRoleView.as_view(), name='host-role-list'),
    path('host/role/add/', HostRoleAddView.as_view(), name='host-role-add'),
    path('host/role/<int:pk>/update/', HostRoleUpdateView.as_view(), name='host-role-update'),
    path('host/role/<int:pk>/delete/', HostRoleDeleteView.as_view(), name='host-role-delete'),

    path('host_sync/', update_host_view, name="host-sync"),
    path('host_index/', HostIndexView.as_view(), name="host_index"),

    path('host_status/<int:pk>/', HostStatusDetailView.as_view(), name='host_status_detail'),
    path('upload/', upload, name='upload'),
    path('project/', ProjectListView.as_view(), name='project'),
    # path('project/', ProjectListView.as_view(), name='project'),
    # path('cloud-plat/', CloudPlatView.as_view(), name='cloud-plat'),
    path('status_list/', HostStatusView.as_view(), name='status_list'),

]