#coding: utf-8
from django.db import models

# Create your models here.

class Host(models.Model):
    id = models.AutoField(primary_key=True)
    #id = models.IntegerField(unique=True,primary_key = True)
    hostname = models.CharField(max_length=50) #主机名
    state = models.CharField(max_length=50,null=True) #状态
    outer_ip = models.CharField(max_length=50) #外网ipo
    inner_ip = models.CharField(max_length=50) #内网ip
    osversion = models.CharField(max_length=50,null=True) #系统版本
    memory = models.CharField(max_length=50,null=True) #内存
    disk = models.CharField(max_length=128,null=True) #磁盘
    cpu_num = models.CharField(max_length=50,null=True) #cpu数量
    #cloudplatform = models.CharField(max_length=50,null=True)
    provider = models.CharField(max_length=50,null=True) #供应商
    host_locate = models.CharField(max_length=50,null=True) #地区
    instance_id = models.CharField(max_length=50,null=True) #实例id
    instance_name = models.CharField(max_length=50,null=True) #实例名字
    virtual_type = models.CharField(max_length=50,null=True) #虚拟化类型
    role = models.CharField(max_length=50,null=True) #角色
    start_time = models.CharField(max_length=50,null=True) #注册时间 DateField
    end_time = models.CharField(max_length=50,null=True) #销毁时间
    project_name = models.CharField(max_length=50,null=True) #项目
    explain = models.CharField(max_length=128, null=True) #说明



    def __str__(self):
        return self.hostname

    class Meta:
        ordering = ["outer_ip"]