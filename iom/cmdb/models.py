#coding: utf-8
from django.db import models

# Create your models here.

class ConfigManage(models.Model):
    gs_ip = models.CharField(max_length=50) #游戏服ip
    gs_zone = models.CharField(max_length=50) #区域
    gs_id = models.CharField(max_length=50) #游戏服id
    gs_alias = models.CharField(max_length=50) #唯一标识符
    gs_accelerate_port = models.CharField(max_length=50) #加速端口
    gs_dir = models.CharField(max_length=50) #游戏服目录
    gs_name = models.CharField(max_length=50) #游戏服名字
    gs_db_name = models.CharField(max_length=50) #游戏服数据库
    gs_db_log_name = models.CharField(max_length=50) #游戏服日志数据库
    gs_db_outer_ip = models.CharField(max_length=50) #数据库外网ip
    gs_db_inner_ip = models.CharField(max_length=50) #游戏服内网ip
    gs_status = models.CharField(max_length=50) #游戏服状态
    gs_open_time = models.CharField(max_length=50) #开服时间
    gs_branch = models.CharField(max_length=50) #分支名
    gs_branch_commit_id = models.CharField(max_length=50) #分支的commit id
    gs_merged = models.CharField(max_length=50) #是否合服
    gs_merged_time = models.CharField(max_length=50) #合服时间
    gs_merged_to_id = models.CharField(max_length=50) #合入id

    def __str__(self):
        return self.gs_name









