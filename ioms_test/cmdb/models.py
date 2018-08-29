#coding: utf-8

from django.db import models
from hostmanage.models import Host
from db.models import MasterDb

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
        return "{}-{}".format(self.status, self.status_explain)

    class Meta:
        ordering = ['id', 'status']


class Tag(models.Model):
    """
    标签，用于部署的时候判断部署的分支。
    """
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=48, null=False, unique=True, verbose_name='标签')
    tag_explain = models.CharField(max_length=128, null=True, blank=True, verbose_name="标签说明")

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ['id']


class GwConfig(models.Model):
    id = models.AutoField(primary_key=True)
    gw_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, related_name="gw_ip_info",
                              verbose_name="host ip's id")
    gw_zone = models.ForeignKey(ZoneName, on_delete=models.SET_NULL, blank=True, null=True, related_name='gw_zone',
                                verbose_name='gw zone')
    gw_dir = models.CharField(max_length=42, blank=True, null=True, verbose_name='gw dir')
    gw_port = models.IntegerField()
    gw_db = models.CharField(max_length=42, blank=True, null=True, verbose_name='database name')
    gw_db_ip = models.ForeignKey(MasterDb, on_delete=models.SET_NULL, blank=True, null=True, related_name="gw_db",
                              verbose_name="main db")


class GsConfig(models.Model):
    id = models.AutoField(primary_key=True)
    used = models.CharField(max_length=50, verbose_name="是否使用")

    gs_zone = models.ForeignKey(ZoneName, on_delete=models.SET_NULL, related_name="gs_zone_name",
                                blank=True, null=True, verbose_name="zone id，安卓 or ios")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_tag",
                            verbose_name="标签字段")
    gs_id = models.IntegerField(verbose_name="游戏服id")
    gs_name = models.CharField(max_length=50, verbose_name="游戏服名字")
    gs_alias = models.CharField(max_length=50, verbose_name="唯一标识符")
    gs_ip = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_ip_info",
                              verbose_name="host ip's id")
    gs_language = models.CharField(max_length=11, blank=True, null=True, verbose_name="语言")

    gs_accelerate_port = models.CharField(max_length=50, verbose_name="加速端口")
    gs_dir = models.CharField(max_length=50, verbose_name="游戏服目录")


    gs_status = models.ForeignKey(GsStatus, on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name="gs_status", verbose_name="gs status id")
    gs_open_time = models.CharField(max_length=50, verbose_name="开服时间")
    # gs_open_time = models.DateTimeField(max_length=50,null=True, verbose_name="开服时间")

    gs_branch = models.CharField(max_length=50, verbose_name="分支名")
    gs_branch_commit_id = models.CharField(max_length=50, verbose_name="分支的commit id")
    gs_merged = models.CharField(max_length=50, verbose_name="是否合服")
    gs_merged_time = models.CharField(max_length=50, verbose_name="合服时间")
    gs_merged_to_id = models.CharField(max_length=50, verbose_name="合入id")
    gs_db_name = models.CharField(max_length=42, blank=True, null=True, verbose_name='database name')
    gs_log_db_name = models.CharField(max_length=42, blank=True, null=True, verbose_name='database log name')
    gs_db = models.ForeignKey(MasterDb, on_delete=models.SET_NULL, blank=True, null=True, related_name="gs_db",
                              verbose_name="main db")

    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")

    def __str__(self):
        return self.gs_name

    class Meta:
        ordering = ['gs_zone', 'gs_id']



