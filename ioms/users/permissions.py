#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 上午11:20
# @Author  : tang
# @FileName: permissions.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import permissions
from django.contrib.sessions.models import Session
class IsValidUser(permissions.BasePermission):
    """allow access to valid user, is active and not expired"""
    message = "必须是SVIP才能访问"

    def has_permission(self, request, view):
        print(request._request.user)
        if request.user.is_staff:
            return True
        return False
        # print(1,request.session.session_key)
        # session_key = request.session.session_key
        # s = Session.objects.get(session_key=session_key)
        # print(s.user)
        # return super(IsValidUser, self).has_permission(request, view) and request._request.user.is_staff



