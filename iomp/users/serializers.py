#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 上午10:41
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com


from .models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(required=False, max_length=100)
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'email')




