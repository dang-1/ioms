#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午5:39
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

# from django.conf.urls import url

# from .views import *

# app_name = 'sitecollect'

# urlpatterns = [

#     #url(r'^hostmanage', include('hostmanage.urls')),
#     #url(r'^index2/$', siteindex, name='siteindex2'),
#     url(r'^siteindex/$', SiteIndex.as_view(), name='siteindex'),
#     url(r'^site_type/$', SiteType.as_view(), name='site_type'),
#     #url(r'^index/api/$', site_index_api, name='siteindexapi'),
#     url(r'^site_type_add/$', SiteTypeAddView.as_view(), name='site_type_add'),
#     url(r'^site_type_change/', SiteTypeNameChangeView.as_view(), name='site_type_change'),
#     #url(r'^addsite', addsite, name='addsite'),
#     #url(r'^deletesite', deletesite, name='deletesite'),

# ]
from django.contrib import admin
from django.urls import path

from .views import SiteIndex, SiteAddView, SiteType, SiteTypeAddView, SiteTypeAddView2

app_name = 'sitecollect'

urlpatterns = [
    path('site_index/', SiteIndex.as_view(), name='site_index'),
    path('site_add/', SiteAddView.as_view(), name='site_add'),
    path('site_type_index/', SiteType.as_view(), name='site_type_index'),
    path('site_type_add/', SiteTypeAddView.as_view(), name='site_type_add'),
    path('site_type/add/', SiteTypeAddView2.as_view(), name='site_type_add2'),
    # path('admin/', admin.site.urls),
    # path('login/', Login.as_view(), name='login'), #ok
    # path('logout/', user_logout, name='logout'),
    # path('register/', Login.as_view(), name='register'),
    # # path('user_list/', Login.as_view(), name='user_list'),
    # path('useradd/', UserAdd.as_view(), name='useradd'),
    # path('user_list/', UserList.as_view(), name='user_list'),
    # # path('login/$', )
]