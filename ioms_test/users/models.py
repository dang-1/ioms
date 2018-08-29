#coding: utf-8
import uuid
from collections import OrderedDict

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ #翻译相关
from django.utils import timezone
# from django.common.mixins import NoDeleteModelMixin
# Create your models here.

__all__ = ['User', 'UserGroup']

def date_expired_default():
    try:
        years = int(settings.DEFAULT_EXPIRED_YEARS)
    except TypeError:
        years = 70
    return timezone.now() + timezone.timedelta(days=365*years)

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    #nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    wechat = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField('UserGroup', related_name='users', blank=True, verbose_name='user group')
    comment = models.TextField(max_length=200, blank=True, verbose_name='comment')
    date_expired = models.DateTimeField(default=date_expired_default, blank=True, null=True,
                                        verbose_name='Date expired')
    created_by = models.CharField(max_length=30, default='', verbose_name='Created by')

    # zabbix_tmp_pass = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.username

    #disable watch password
    @property
    def password_raw(self):
        raise AttributeError('Password raw is not a readable attribute')

    #set password
    @password_raw.setter  # 设置密码
    def password_raw(self, password_raw_):
        self.set_password(password_raw_)
    #change password
    def reset_password(self, new_password):
        self.set_password(new_password)
        self.save()

    @property
    def is_valied(self):
        #if self.is_active and not self.is_expired:
        #    return True
        return True
    def get_full_name(self):
        return self.email


    # save info
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.username
        #if self.username == 'admin':
        #    self.role = 'Admin'
        #    self.is_active = True

        super().save(*args, **kwargs)

    def to_json(self):
        return OrderedDict({
            'id': self.id,
            'username': self.username,
            #'name': self.name,
            'email': self.email,
            #'is_active': self.is_active,
            'is_superuser': self.is_superuser,
            #'role': self.get_role_display(),
            #'groups': [group.name for group in self.groups.all()],
            #'wechat': self.wechat,
            'phone': self.phone,
            #'comment': self.comment,
            #'date_expired': self.date_expired.strftime('%Y-%m-%d %H:%M:%S') if self.date_expired is not None else None
        })
    class Meta:
        ordering = ['username']


class UserGroup(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name='group name')
    comment = models.CharField(max_length=123, blank=True, verbose_name='comment')
    date_created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='date created')
    created_by = models.CharField(max_length=100, null=True, blank=True, verbose_name="who create")

    def __str__(self):
        return self.name




