#coding: utf-8
from django.db import models

__all__ = ['HostRole', 'ProjectName', 'CloudPlat', 'HostStatus', 'Host']

class HostRole(models.Model):
	'''
	host role name
	'''
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=48, null=False, unique=True, verbose_name="角色")

    def __str__(self):
        return self.role


class ProjectName(models.Model):
	'''
	project name
	'''
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=48, null=False, unique=True, verbose_name="项目名")

    def __str__(self):
        return self.project_name


class CloudPlat(models.Model):
	'''
	cloud platfrom
	'''
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=48, null=False, verbose_name="提供商")
    cloud_platform_name = models.CharField(max_length=48, null=False, verbose_name="云平台名字")
    locate = models.CharField(max_length=48, null=True, verbose_name="国家")
    city = models.CharField(max_length=48, null=True, verbose_name="城市")

    def __str__(self):
        return self.cloud_platform_name


class HostStatus(models.Model):
	'''
	host status
	'''
	id = models.AutoField(primary_key=True)
	status = models.CharField(max_length=48, null=False, unique=True, verbose_name='状态')


class Host(models.Model):
	'''
	single host
	'''
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=50, unique=True, verbose_name="主机名")
    # state = models.CharField(max_length=50,null=True, verbose_name="状态")
    status = models.ForeignKey(HostStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='状态')
    outer_ip = models.CharField(max_length=50, verbose_name="外网ip")
    inner_ip = models.CharField(max_length=50, verbose_name="内网ip")
    osversion = models.CharField(max_length=50,null=True, verbose_name="系统版本")
    memory = models.CharField(max_length=50,null=True, verbose_name="内存")
    disk = models.CharField(max_length=128,null=True, verbose_name="磁盘")
    cpu_num = models.CharField(max_length=50,null=True, verbose_name="cpu数量")
    platfrom = models.ForeignKey(CloudPlat, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="区域")
    # provider = models.CharField(max_length=50,null=True) #供应商
    # host_locate = models.CharField(max_length=50,null=True) #地区
    instance_id = models.CharField(max_length=50,null=True, verbose_name="实例id")
    instance_name = models.CharField(max_length=50,null=True, verbose_name="实例名字")
    virtual_type = models.CharField(max_length=50,null=True, verbose_name="虚拟化类型")
    # role = models.CharField(max_length=50,null=True, verbose_name="区域") #角色
    role = models.ManyToManyField(HostRole, verbose_name='角色')
    start_time = models.CharField(max_length=50,null=True, verbose_name="注册时间 DateField")
    end_time = models.CharField(max_length=50,null=True, verbose_name="销毁时间")
    # project_name = models.CharField(max_length=50,null=True) #项目
    project = models.ForeignKey(ProjectName, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="项目")
    explain = models.CharField(max_length=128, null=True, verbose_name="说明")

    def __str__(self):
        return self.hostname

    class Meta:
        ordering = ["outer_ip"]


