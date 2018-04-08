#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午5:23
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django.conf.urls import url

from .views import *

app_name = 'users'

urlpatterns = [
    url(r'^register/$', register, name='register'),
    #url(r'^login/$', name='login'),

    #url(r'^logout/$', logout, name='login'),
    #url(r'^password_change/$', , name='login'),
    #url(r'^password_change/done/$', login, name='login'),
    #url(r'^password_reset/$', login, name='login'),
    #url(r'^password_reset/done/$', login, name='login'),

]