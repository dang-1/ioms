#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 上午11:13
# @Author  : tang
# @FileName: authentication.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework.authentication import BaseAuthentication
from django.contrib.sessions.models import Session
from .models import User
from rest_framework import exceptions
# class Authtication(object):
#     def authenticate(self, request):
#         token = request._request.GET.get('token')
#         token_obj =


class Authtication(BaseAuthentication):
    def authenticate(self, request):
        # session_key = request.session.session_key
        session_key = request._request.GET.get('token')
        print(session_key)
        try:
            s = Session.objects.get(session_key=session_key)
        except:
            raise exceptions.AuthenticationFailed("session key get error")
        print(1, request._request.user)
        user_id = s.get_decoded()['_auth_user_id']
        user = User.objects.get(pk=user_id)
        if not user_id:
            raise exceptions.AuthenticationFailed('用户认证失败')

        # print(s.expire_date)

        # token = request._request.GET.get('token')
        # token_obj = models.UserToken.objects.filter(token=token).first()
        # if not token_obj:
        #     raise exception.AuthenticationFailed('用户认证失败')
        #在rest_framework内部会将整个两个字段赋值给request，以供后续操作使用
        return (user.name, session_key)
    def authentication_header(self, request):
        return 'Basic realm="api"'
