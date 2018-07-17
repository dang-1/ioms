#coding: utf-8

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

# from rest_framework import viewsets
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404

# from .serializers import HostSerializer

from .models import *

class DbTypeView(LoginRequiredMixin, ListView):
    template_name = 'db/type_list.html'
    context_object_name = 'db_type_list'
    model = DbType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db config page'
        return context


class DbListView(LoginRequiredMixin, ListView):
    template_name = 'db/db_list.html'
    context_object_name = 'db_list'
    model =  MasterDb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db config page'
        return context



