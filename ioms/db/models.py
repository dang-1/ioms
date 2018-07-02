#coding: utf-8
from django.db import models
from hostmanage.models import Host


class DbType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=48, null=False, verbose_name="type")
    explain = models.CharField(max_length=96, blank=True, verbose_name="说明")


class MasterDb(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(DbType, on_delete=models.SET_NULL, blank=True, null=True, related_name="type_info",
                             verbose_name="db type")
    host_info = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, related_name="host_info",
                              verbose_name="host ip's id")
    alias = models.CharField(max_length=48, blank=True, verbose_name="别名")
    db_port = models.CharField(max_length=42, default=3306, verbose_name='database port')
    # db_slave = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="slave_info", null=True, blank=True,
    #                              verbose_name="从库")
    status = models.CharField(max_length=42, null=False, verbose_name='database status, online of offline')
    open_time = models.CharField(max_length=42, null=False, blank=True, verbose_name='database open time')

    def __str__(self):
        return self.alias

    class Meta:
        ordering = ['id', 'alias']


class SlaveDb(models.Model):
    id = models.AutoField(primary_key=True)
    host_info = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, related_name="slave_host_info",
                              verbose_name="host ip's id")
    alias = models.CharField(max_length=48, blank=True, verbose_name="别名")
    db_port = models.CharField(max_length=42, default=3306, verbose_name='database port')
    # db_master = models.ForeignKey(MasterDb, on_delete=models.SET_NULL, related_name="slave_info", null=True, blank=True,
    #                              verbose_name="从库")
    db_master = models.OneToOneField(MasterDb, on_delete=models.SET_NULL, null=True, verbose_name="master info")
    status = models.CharField(max_length=42, null=False, verbose_name='database status, online of offline')
    open_time = models.CharField(max_length=42, null=False, blank=True, verbose_name='database open time')

    def __str__(self):
        return self.alias

    class Meta:
        ordering = ['id', 'alias']
        # unique_together = ('host_info', 'db_port')



