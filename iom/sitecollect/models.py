#coding: utf-8
from django.db import models

# Create your models here.

class SiteType(models.Model):
    typename = models.CharField(max_length=60)
    typeid = models.CharField(max_length=60)

class SiteCollect(models.Model):
    sitename = models.CharField(max_length=60)
    siteurl = models.CharField(max_length=60)
    typeid = models.CharField(max_length=60)

    def __str__(self):
        return self.sitename


class SiteTypeR(models.Model):
    id = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=60)

    def __str__(self):
        return self.typename

class SiteCollectR(models.Model):
    typeid = models.ForeignKey(SiteTypeR, on_delete=models.CASCADE)
    sitename = models.CharField(max_length=60)
    siteurl = models.CharField(max_length=60)

    def __str__(self):
        return self.sitename

