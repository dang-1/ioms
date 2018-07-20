#coding: utf-8
from django.db import models


# Create your models here.
class Blog(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=30, verbose_name="标题")
   content = models.TextField(max_length=300, verbose_name="内容")



