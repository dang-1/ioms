#!/usr/bin/env python
#coding: utf-8

import uuid
from django.conf import setting

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


