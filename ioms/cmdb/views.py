#coding: utf-8

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# from .serializers import HostSerializer

from .models import *
# from .form import 
class GsStatusView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/gs_status.html'
    context_object_name = 'gs_status_list'
    model = GsStatus
    paginate_by = 30

    def get_context_data(self, **kwargs):
        # context = super(GsStatusView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: gs status page'
        return context


class ZoneNameView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/zone_name.html'
    context_object_name = 'zone_name_list'
    model = ZoneName

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: zone name page'
        return context


class GsListView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/gs_list.html'
    context_object_name = 'gs_config_list'
    model = ConfigManage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: gs config page'
        return context

