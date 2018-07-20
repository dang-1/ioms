#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 下午3:30
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

# from django.conf.urls import url
#
# from . import views
#
# urlpatterns = [
#
#    url(r'^$', views.index,name='blog_index'),
#
#    url(r'^add/$', views.add,name='blog_add'),
#
#    url(r'^list/$', views.list,name='blog_list'),
#
#    url(r'^detail/(?P<blog_id>\d+)$', views.detail,name='blog_detail'),
#
#    url(r'^delete/(?P<blog_id>\d+)$', views.delete,name='blog_delete'),
#
#    url(r'^modify/(?P<blog_id>\d+)$', views.modify,name='blog_modify'),
#
# ]

from django.urls import path

from .views import IndexView

app_name = 'blog'

urlpatterns = [
    path("", IndexView.as_view(), name="blog_index"),
    # path('host_sync/', update_host_view, name="host_sync"),
    # path('host_index/', HostIndexView.as_view(), name="host_index"),
    # path('status_list/', HostStatusView.as_view(), name='status_list'),
    # path('host_status/<int:pk>/', HostStatusDetailView.as_view(), name='host_status_detail'),
    # path('upload/', upload, name='upload')
    #path('site_type/<int:pk>/', SiteTypeDetailView.as_view(), name='site_type_detail'),
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