#coding: utf-8

from django.db import models
from hostmanage.models import Host




class Rule(models.Model):
    '''
    一般规则
    '''
    id = models.AutoField(primary_key=True)
    host = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='主机外键')
    # rule line
    rule = models.CharField(max_length=1200, null=False, verbose_name='规则，整行')
    status = models.CharField(null=True, max_length=6, verbose_name='状态')
    modify_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')




class DefaultRule(models.Model):
    '''
    默认规则
    '''
    id = models.AutoField(primary_key=True)
    host = models.ForeignKey(Host, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='主机外键')
    input_rule = models.CharField(max_length=32, verbose_name='默认入站规则')
    output_rule = models.CharField(max_length=32, verbose_name='默认出站规则')
    forward_rule = models.CharField(max_length=32, verbose_name='默认过滤规则')





