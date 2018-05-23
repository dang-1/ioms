#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午4:21
# @Author  : tang
# @FileName: serializers.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework import serializers

from .models import ConfigManage

class ConfigMangeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ConfigManage
		fields = (
            'id',
            'used',
            'gs_id',
        )

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
