#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:33
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.urls import path
# from rest_framework import routers

from ..views import MergeListView, update_merge_info, update_all_merge_info

#status
from ..views import GsStatusView, GsStatusAddView, GsStatusUpdateView
#zone name
from ..views import ZoneNameView,ZoneNameAddView,ZoneNameUpdateView, ZoneNameDeleteView
#tag
from ..views import TagListView, TagDetailView, TagUpdateView, TagAddView, TagDeleteView

#gs
from ..views import GsListView, GsDetailView, GsUpdateView, GsAddView, GsStatusDeleteView

app_name = 'cmdb'

urlpatterns = [
    path('gs-status/list/', GsStatusView.as_view(), name='gs-status-list'),
    path('gs-status/add/', GsStatusAddView.as_view(), name='gs-status-add'),
    path('gs-status/<int:pk>/update/', GsStatusUpdateView.as_view(), name='gs-status-update'),
    path('gs-status/<int:pk>/delete/', GsStatusDeleteView.as_view(), name='gs-status-delete'),

    path('zone-name/list/', ZoneNameView.as_view(), name='zone-name-list'),
    path('zone-name/add/', ZoneNameAddView.as_view(), name='zone-name-add'),
    path('zone-name/<int:pk>/update/', ZoneNameUpdateView.as_view(), name='zone-name-update'),
    path('zone-name/<int:pk>/delete/', ZoneNameDeleteView.as_view(), name='zone-name-delete'),

    path('tag/list/', TagListView.as_view(), name='tag-list'),
    path('tag/add/', TagAddView.as_view(), name='tag-add'),
    path('tag/<int:pk>/detail/', TagDetailView.as_view(), name='tag-detail'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),

    path('gs/list/', GsListView.as_view(), name='gs-list'),
    path('gs/add/', GsAddView.as_view(), name='gs-add'),
    path('gs/<int:pk>/detail/', GsDetailView.as_view(), name='gs-detail'),
    path('gs/<int:pk>/update/', GsUpdateView.as_view(), name='gs-update'),

    # path('gs-list/', GsListView.as_view(), name='gs-list1'),
    path('merge-info/', MergeListView.as_view(), name='merge-info'),
    path('merge-info/update/', update_all_merge_info, name='update-all-info-merge'),
    path('merge-info/<int:pk>/update/', update_merge_info, name='update-one-info-merge'),
]