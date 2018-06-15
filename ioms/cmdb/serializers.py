#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午4:21
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from .models import ConfigManage, DbConfig

# class ConfigMangeSerializer(serializers.HyperlinkedModelSerializer):
class ConfigMangeSerializer(serializers.ModelSerializer):
    class Meta:
        # gszone_display = serializers.SerializerMethodField()
        gs_zone_name = serializers.RelatedField(source='gs_zone', read_only=True)
        # db_display = serializers.RelatedField(many=True)
        model = ConfigManage
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
    class Meta:
        model = DbConfig
        fields = ('id', 'host_ip', 'db_name')
        depth = 1

class GsConfigSerializer(serializers.ModelSerializer):
    # config_manage = serializers.StringRelatedField(many=True) #返回str
    config_manage = DbConfigSerializer(many=True, read_only=True) #返回对应的信息
    # config_manage = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #返回pk

    class Meta:
        model = ConfigManage
        fields = "__all__"
        depth = 1



# class UserSerializer(ModelSerializer):
#     groups_display = serializers.SerializerMethodField()
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'is_staff', 'name', 'groups_display', 'groups')
#         depth = 1
#         read_only_fields = ('id',)
#     @staticmethod
#     def get_groups_display(obj):
#         return ",".join([x.name for x in obj.groups.all()])
# used = models.CharField(max_length=50, verbose_name="是否使用")
#     gs_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="host ip's id")
#     gs_zone = models.ForeignKey(ZoneName, on_delete=models.SET_NULL, related_name="gs_zone_name_set",
#                                 blank=True, null=True, verbose_name="zone id")
#     gs_id = models.CharField(max_length=50, verbose_name="游戏服id")
#     gs_alias = models.CharField(max_length=50, verbose_name="唯一标识符")
#     gs_accelerate_port = models.CharField(max_length=50, verbose_name="加速端口")
#     gs_dir = models.CharField(max_length=50, verbose_name="游戏服目录")
#     gs_name = models.CharField(max_length=50, verbose_name="游戏服名字")
#     gs_db = models.ForeignKey(DbConfig, on_delete=models.SET_NULL, related_name="gs_db_set", blank=True, null=True,
#                               verbose_name="gs db id")
#     gs_log_db = models.ForeignKey(DbConfig, on_delete=models.SET_NULL, related_name="gs_log_db_set", blank=True,
#                                   null=True, verbose_name="gs log db id")
#     gs_status = models.ForeignKey(GsStatus, on_delete=models.SET_NULL, blank=True, null=True,
#                                   verbose_name="gs status id")
#     gs_open_time = models.CharField(max_length=50, verbose_name="开服时间")
#     gs_branch = models.CharField(max_length=50, verbose_name="分支名")
#     gs_branch_commit_id = models.CharField(max_length=50, verbose_name="分支的commit id")
#     gs_merged = models.CharField(max_length=50, verbose_name="是否合服")
#     gs_merged_time = models.CharField(max_length=50, verbose_name="合服时间")
#     gs_merged_to_id = models.CharField(max_length=50, verbose_name="合入id")
