#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 上午9:37
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com


from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User, UserGroup


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(ModelSerializer):
    groups_display = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'name', 'groups_display', 'groups')
        depth = 1
        read_only_fields = ('id',)
    @staticmethod
    def get_groups_display(obj):
        return ",".join([x.name for x in obj.groups.all()])


class GroupSerializer(ModelSerializer):
    users_display = serializers.SerializerMethodField()
    class Meta:
        model = UserGroup
        # fields = ('id', 'name', 'comment', 'date_created', 'created_by', 'users_display')
        exclude = []
    def get_field_names(self, declared_fields, info):
        fields = super(GroupSerializer, self).get_field_names(declared_fields, info)
        fields.extend(['users_display', ])
        return fields
    @staticmethod
    def get_users_display(obj):
        return ",".join([x.name for x in obj.users.all()])




