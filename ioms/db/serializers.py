#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 上午9:44
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

# from rest_framework.views import APIView
from rest_framework import serializers
from .models import MasterDb, SlaveDb



class SlaveDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlaveDb
        fields = ["alias",]

class MasterDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDb
        fields = ["id","type", "host_info", "alias", "db_port", "status"]
        depth = 1


#nested relationships

class MasterDbSerializer2(serializers.ModelSerializer):
    slave = SlaveDbSerializer(many=True,read_only=True)

    class Meta:
        model = MasterDb
        fields = ["id","type", "host_info", "alias", "db_port", "status", "slave"]
        depth = 1

