#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午5:39
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.conf.urls import url

from .views import *

app_name = 'sitecollect'

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^hostmanage', include('hostmanage.urls')),
    url(r'^index/$', siteindex, name='siteindex'),
    url(r'^index2/$', siteindex2.as_view(), name='siteindex2'),
    url(r'^index/api/$', site_index_api, name='siteindexapi'),
    url(r'^managesite', managesite, name='managesite'),
    url(r'^sitetypemanage', sitetypemanage, name='typemanage'),
    url(r'^addsite', addsite, name='addsite'),
    url(r'^deletesite', deletesite, name='deletesite'),

]