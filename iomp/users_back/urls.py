#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午1:59
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django.conf.urls import url

from .views import Login, user_logout, UserList, UserAdd, register


app_name = 'users'

urlpatterns = [
    #url(r'^login/$', login, name='login'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', user_logout, name='logout'),
    #url(r'^index/api/$', site_index_api, name='siteindexapi'),
    url(r'^user_list', UserList.as_view(), name='user_list'),
    url(r'^useradd', UserAdd.as_view(), name='user_add'),
    #url(r'^addsite', addsite, name='addsite'),
    #url(r'^deletesite', deletesite, name='deletesite'),

]