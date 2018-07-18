#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:33
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.urls import path
# from rest_framework import routers

from ..views import GsStatusView, ZoneNameView, MergeListView, \
    update_merge_info, update_all_merge_info


#tag
from ..views import TagListView, TagDetailView, TagUpdateView, TagAddView, TagDeleteView

#gs
from ..views import GsListView, GsDetailView, GsUpdateView

app_name = 'cmdb'


urlpatterns = [
    path('tag/list/', TagListView.as_view(), name='tag-list'),
    path('tag/add/', TagAddView.as_view(), name='tag-add'),
    path('tag/<int:pk>/detail/', TagDetailView.as_view(), name='tag-detail'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),

    path('gs/list/', GsListView.as_view(), name='gs-list'),
    path('gs/<int:pk>/detail/', GsDetailView.as_view(), name='gs-detail'),
    path('gs/<int:pk>/update/', GsUpdateView.as_view(), name='gs-update'),


    path('gs-status/', GsStatusView.as_view(), name='gs-status'),
    path('zone-name/', ZoneNameView.as_view(), name='zone-name'),
    # path('gs-list/', GsListView.as_view(), name='gs-list1'),
    path('merge-info/', MergeListView.as_view(), name='merge-info'),
    path('merge-info/update/', update_all_merge_info, name='update-all-info-merge'),
    path('merge-info/<int:pk>/update/', update_merge_info, name='update-one-info-merge'),
    # path('db-list/', DbListView.as_view(), name='db-list'),
    # path('host_index/', HostIndexView.as_view(), name="host_index"),
    # path('status_list/', StatusView.as_view(), name='status_list'),
    # path('site_index/', SiteIndex.as_view(), name='site_index'),
    # path('site_add/', SiteAddView.as_view(), name='site_add'),
    # path('site_type_index/', SiteType.as_view(), name='site_type_index'),
    # path('site_type_add/', SiteTypeAddView.as_view(), name='site_type_add'),
]