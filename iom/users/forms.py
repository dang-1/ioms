#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午5:22
# @Author  : tang
# @FileName: forms.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com




from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
