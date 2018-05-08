#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午1:59
# @Author  : tang
# @FileName: urls.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

# from django.contrib import admin
from django.urls import path

from .. import views
# from .views import Login, user_logout, UserAdd, UserList

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'), #ok
    path('logout/', views.user_logout, name='logout'), #ok
    path('register/', views.Login.as_view(), name='register'),
    path('user_add/', views.UserAdd.as_view(), name='user_add'), #ok
    path('user_list/', views.UserList.as_view(), name='user_list'), #ok
]