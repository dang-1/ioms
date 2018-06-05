#coding: utf-8

from django.db import models
from hostmanage.models import Host

__all__ = ["GsStatus", "ZoneName", "DbConfig", "ConfigManage"]


class ZoneName(models.Model):
    '''
    gs zone
    eg: ch un korea 
    '''
    id = models.AutoField(primary_key=True)
    contry = models.CharField(max_length=48, null=True)
    zone_name = models.CharField(max_length=48, null=False)

    def __str__(self):
        return self.zone_name

    class Meta:
        ordering = ["zone_name"]


class GsStatus(models.Model):
    '''
    gs status
    '''
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=48, null=False, unique=True, verbose_name='字段id')
    status_explain = models.CharField(max_length=48, blank=True, verbose_name='字段说明')

    def __str__(self):
        return self.status






class ConfigManage(models.Model):
    id = models.AutoField(primary_key=True)
    used = models.CharField(max_length=50, verbose_name="是否使用")
    gs_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="host ip's id")
    gs_zone = models.ForeignKey(ZoneName, on_delete=models.SET_NULL, related_name="gs_zone_name_set",
                                blank=True, null=True, verbose_name="zone id")
    gs_id = models.CharField(max_length=50, verbose_name="游戏服id")
    gs_alias = models.CharField(max_length=50, verbose_name="唯一标识符")
    gs_accelerate_port = models.CharField(max_length=50, verbose_name="加速端口")
    gs_dir = models.CharField(max_length=50, verbose_name="游戏服目录")
    gs_name = models.CharField(max_length=50, verbose_name="游戏服名字")
    # gs_db = models.ForeignKey(DbConfig, on_delete=models.SET_NULL, related_name="gs_db_set", blank=True, null=True,
    #                           verbose_name="gs db id")
    # gs_log_db = models.ForeignKey(DbConfig, on_delete=models.SET_NULL, related_name="gs_log_db_set", blank=True,
    #                               null=True, verbose_name="gs log db id")
    gs_status = models.ForeignKey(GsStatus, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name="gs status id")
    gs_open_time = models.CharField(max_length=50, verbose_name="开服时间")
    gs_branch = models.CharField(max_length=50, verbose_name="分支名")
    gs_branch_commit_id = models.CharField(max_length=50, verbose_name="分支的commit id")
    gs_merged = models.CharField(max_length=50, verbose_name="是否合服")
    gs_merged_time = models.CharField(max_length=50, verbose_name="合服时间")
    gs_merged_to_id = models.CharField(max_length=50, verbose_name="合入id")

    def __str__(self):
        return self.gs_name

    class Meta:
        ordering = ['gs_zone', 'gs_id']


class DbConfig(models.Model):
    '''
    database config
    '''
    id = models.AutoField(primary_key=True)
    host_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="host ip's id")
    db_user = models.CharField(max_length=42, verbose_name='database user')
    db_port = models.CharField(max_length=42, default='3306', verbose_name='database port')
    db_name = models.CharField(max_length=42, verbose_name='database name')
    status = models.CharField(max_length=42, null=False, verbose_name='database status')
    config_manage = models.ForeignKey(ConfigManage, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name='db_config')

    def __str__(self):
        return self.db_name
    class Meta:
        ordering = ['host_ip', 'db_name']
