#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午4:21
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from .models import GsConfig, DbConfig

# class ConfigMangeSerializer(serializers.HyperlinkedModelSerializer):
class ConfigMangeSerializer(serializers.ModelSerializer):
    class Meta:
        # gszone_display = serializers.SerializerMethodField()
        gs_zone_name = serializers.RelatedField(source='gs_zone', read_only=True)
        # db_display = serializers.RelatedField(many=True)
        model = GsConfig
        depth = 1
        # fields = "__all__"
        fields = (
            'id',
            'used',
            'gs_id',
            # 'gs_zone_name',
            # 'gszone_display',
            'gs_id',
            'gs_alias',
            'gs_accelerate_port',
            'gs_dir',
            'gs_name',
            'gs_status',
            'gs_open_time',
            'gs_branch',
            'gs_branch_commit_id',
            'gs_merged',
            'gs_merged_time',
            'gs_merged_to_id',
            # 'db_display',
        )
        # @staticmethod
        # def get_gszone_display(obj):
        #     return [x.id for x in obj.gs_zone]
        @staticmethod
        def get_db_display(obj):
            return ",".join([x.db_name for x in obj.dbconfig_set.all()])


class DbConfigSerializer(serializers.ModelSerializer):

    # master_outer_ip = serializers.SlugRelatedField(many=True, read_only=True, slug_field="outer_ip")
    master_outer_ip = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    class Meta:
        model = DbConfig
        fields = ("id","db_port", "status", "open_time", "master_outer_ip")
        # fields = "__all__"
        depth = 1

    def get_master_outer_ip(self, obj):
        return obj.master_ip.outer_ip

# class DbConfigSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DbConfig
#         fields = ('id', 'host_ip', 'db_name')
#         depth = 1


class GsConfigSerializer(serializers.ModelSerializer):
    # config_manage = serializers.StringRelatedField(many=True) #返回str
    config_manage = DbConfigSerializer(many=True, read_only=True) #依赖上一个序列化，返回对应的信息
    # config_manage = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #返回pk

    class Meta:
        model = GsConfig
        fields = "__all__"
        depth = 1




