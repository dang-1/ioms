#coding: utf-8

from django.db import models
from hostmanage.models import Host

__all__ = ["GsStatus", "ZoneName", "DbConfig", "GsConfig"]


class ZoneName(models.Model):
    '''
    gs zone
    eg: ch un korea 
    '''
    id = models.AutoField(primary_key=True)
    # contry = models.CharField(max_length=48, null=True, verbose_name="国家")
    zone_name = models.CharField(max_length=48, null=False, verbose_name="区域")
    zone_name_explain = models.CharField(max_length=48, blank=True, verbose_name='zone说明')

    def __str__(self):
        return self.zone_name

    class Meta:
        ordering = ["id"]


class GsStatus(models.Model):
    '''
    gs status
    '''
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=48, null=False, unique=True, verbose_name='字段id')
    status_explain = models.CharField(max_length=48, blank=True, verbose_name='字段说明')

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['id', 'status']


class Tag(models.Model):
    """
    标签
    """
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=48, null=False, unique=True, verbose_name='标签')


# class KeConfig(models.Model):
#     id = models.AutoField(primary_key=True)
#     used = models.CharField(max_length=50, verbose_name="是否使用")
#     gs_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_ip_info",
#                               verbose_name="host ip's id")
#     gs_zone = models.ForeignKey(ZoneName, on_delete=models.SET_NULL, related_name="gs_zone_name",
#                                 blank=True, null=True, verbose_name="zone id，安卓 or ios")
#     tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_tag",
#                             verbose_name="标签字段")

class DbConfig(models.Model):
    '''
    database config
    not use
    '''
    id = models.AutoField(primary_key=True)
    master_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name="master_ip_info", verbose_name="master ip's id")
    slave_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name="slave_ip_info", verbose_name="slave ip's id")
    # host_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True,
    #                             related_name="host_ip", verbose_name="host ip's id")
    # db_user = models.CharField(max_length=42, verbose_name='database user')
    # db_type = models.CharField(max_length=42, verbose_name="数据库类型")

    db_port = models.CharField(max_length=42, default='3306', verbose_name='database port')
    # db_name = models.CharField(max_length=42, verbose_name='database name')
    status = models.CharField(max_length=42, null=False, verbose_name='database status, online of offline')
    open_time = models.CharField(max_length=42, null=False, blank=True, verbose_name='database open time')
    # config_manage = models.ForeignKey(GsConfig, on_delete=models.SET_NULL, blank=True, null=True,
    #                                   related_name="config_manage", verbose_name='db_config')
    # db_type = models.CharField(max_length=48, null=True, verbose_name='数据库用途')

    def __str__(self):
        return str(self.id)
    class Meta:
        ordering = ['id']

class GsConfig(models.Model):
    id = models.AutoField(primary_key=True)
    used = models.CharField(max_length=50, verbose_name="是否使用")
    gs_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_ip_info",
                              verbose_name="host ip's id")
    gs_zone = models.ForeignKey(ZoneName, on_delete=models.SET_NULL, related_name="gs_zone_name",
                                blank=True, null=True, verbose_name="zone id，安卓 or ios")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_tag",
                            verbose_name="标签字段")
    gs_id = models.IntegerField(verbose_name="游戏服id")
    gs_alias = models.CharField(max_length=50, verbose_name="唯一标识符")
    gs_accelerate_port = models.CharField(max_length=50, verbose_name="加速端口")
    gs_dir = models.CharField(max_length=50, verbose_name="游戏服目录")
    gs_name = models.CharField(max_length=50, verbose_name="游戏服名字")

    gs_status = models.ForeignKey(GsStatus, on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name="gs_status", verbose_name="gs status id")
    gs_open_time = models.CharField(max_length=50, verbose_name="开服时间")

    gs_branch = models.CharField(max_length=50, verbose_name="分支名")
    gs_branch_commit_id = models.CharField(max_length=50, verbose_name="分支的commit id")
    gs_merged = models.CharField(max_length=50, verbose_name="是否合服")
    gs_merged_time = models.CharField(max_length=50, verbose_name="合服时间")
    gs_merged_to_id = models.CharField(max_length=50, verbose_name="合入id")
    gs_db_name = models.CharField(max_length=42, blank=True, null=True, verbose_name='database name')
    gs_log_db_name = models.CharField(max_length=42, blank=True, null=True, verbose_name='database log name')
    gs_db_ip = models.ForeignKey(DbConfig, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name="gs_db_ip_info", verbose_name="db ip's id")
    gs_db_slave_ip = models.ForeignKey(DbConfig, on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name="gs_db_slave_ip_info", verbose_name="db ip's id")

    # create_time =
    # update_time =

    def __str__(self):
        return self.gs_name

    class Meta:
        ordering = ['gs_zone', 'gs_id']



