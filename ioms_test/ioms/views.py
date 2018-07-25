#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午1:54
# @Author  : tang
# @FileName: views.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# @login_required(login_url='/users/login')
# def IndexView(request):
#     # if request.user.is_authenticated:
#     #     print('auth ok')
#     # else:
#     #     print("auth fail")
#     title_name = 'index'
#     template_name = 'index2.html'
#
#     # def get(request):
#     #     pass
#     return render(request, template_name)

class IndexView(TemplateView):
    template_name = 'adminlte/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title_name'] = 'site index page'
        return context




class IndexView2(LoginRequiredMixin, TemplateView):
    template_name = 'index2.html'

    def get(self, request, *args, **kwargs):
        return super(IndexView2, self).get(request, *args, **kwargs, )

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: index page'
        return context

    # @login_required(login_url='/users/login')
    # def dispatch(self):
    #     pass