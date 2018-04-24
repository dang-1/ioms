#coding: utf-8
from django.db import models

# Create your models here.

__all__ = ["SiteType", "SiteCollect"]

class SiteType(models.Model):
    '''
    site type
    '''
    typename = models.CharField(max_length=60, null=False, unique=True, verbose_name="网址类型")

    def __str__(self):
    	return self.typename


class SiteCollect(models.Model):
    '''
    site collect
    '''
    sitename = models.CharField(max_length=60, null=False, unique=True, verbose_name="链接名称")
    siteurl = models.CharField(max_length=60, null=False, unique=True, verbose_name="链接地址")
    typeid = models.ForeignKey(SiteType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="名称")

    # def save(self, *args, **kwargs):
    # 	# if not self.sitename or not siteurl or not self.typeid:
    # 	super().save(*args, **kwargs)

    def __str__(self):
        return self.sitename