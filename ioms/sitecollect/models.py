#coding: utf-8
from django.db import models
from django.urls import reverse

# Create your models here.

__all__ = ["SiteType", "SiteCollect"]




class SiteTypeModel(models.Model):
    '''
    site type
    '''
    id = models.AutoField(primary_key=True)
    site_type_name = models.CharField(max_length=60, null=False, unique=True, verbose_name="网址类型")

    def __str__(self):
        return self.site_type_name

    def get_absolute_url(self):
        return reverse("sitecollect:site_type_detail", kwargs={'pk': self.id})

    class Meta:
        ordering = ['id']


class SiteCollectModel(models.Model):
    '''
    site collect
    '''
    sitename = models.CharField(max_length=60,default='test', unique=True, verbose_name="链接名称")
    siteurl = models.CharField(max_length=60, default='test',unique=True, verbose_name="链接地址")
    typeid = models.ForeignKey(SiteTypeModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="名称")
    #status = models.ForeignKey(HostStatus, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='状态')

    # def save(self, *args, **kwargs):
    # 	# if not self.sitename or not siteurl or not self.typeid:
    # 	super().save(*args, **kwargs)

    def __str__(self):
        return self.sitename

    class Meta:
        ordering = ['typeid']


