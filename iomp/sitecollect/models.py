#coding: utf-8
from django.db import models

# Create your models here.

class SiteType(models.Model):
    typename = models.CharField(max_length=60)
    #typeid = models.CharField(max_length=60)

class SiteCollect(models.Model):
    sitename = models.CharField(max_length=60)
    siteurl = models.CharField(max_length=60)
    #typeid = models.CharField(max_length=60)
    typeid = models.ForeignKey(SiteType)

    def __str__(self):
        return self.sitename