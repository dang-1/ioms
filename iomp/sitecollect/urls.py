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
    #url(r'^index2/$', siteindex, name='siteindex2'),
    url(r'^siteindex/$', SiteIndex.as_view(), name='siteindex'),
    url(r'^site_type/$', SiteType.as_view(), name='site_type'),
    #url(r'^index/api/$', site_index_api, name='siteindexapi'),
    url(r'^site_type_add/$', SiteTypeAddView.as_view(), name='site_type_add'),
    url(r'^site_type_change/', SiteTypeNameChangeView.as_view(), name='site_type_change'),
    #url(r'^addsite', addsite, name='addsite'),
    #url(r'^deletesite', deletesite, name='deletesite'),

]