#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午1:59
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

# from django.contrib import admin
from django.urls import path

from .views import Login, user_logout, UserAdd, UserList

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'), #ok
    path('logout/', user_logout, name='logout'), #ok
    # path('register/', Login.as_view(), name='register'),
    path('user_add/', UserAdd.as_view(), name='user_add'), #ok
    path('user_list/', UserList.as_view(), name='user_list'), #ok
]