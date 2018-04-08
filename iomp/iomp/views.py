#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午1:54
# @Author  : tang
# @FileName: views.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/users/login')
def IndexView(request):
    # if request.user.is_authenticated:
    #     print('auth ok')
    # else:
    #     print("auth fail")
    template_name = 'index.html'
    return render(request, template_name)

