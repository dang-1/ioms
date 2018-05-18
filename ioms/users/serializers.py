#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 上午9:37
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from .models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')



