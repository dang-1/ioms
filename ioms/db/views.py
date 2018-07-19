#coding: utf-8

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from rest_framework import viewsets
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404

# from .serializers import HostSerializer

from .models import *
from .form import DbTypeForm, MasterDbForm, SlaveDbForm


#================================db type begin==============================================

class DbTypeListView(LoginRequiredMixin, ListView):
    template_name = 'db/db_type_list.html'
    context_object_name = 'db_type_list'
    model = DbType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db type list page'
        return context


class DbTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = "db/db_type_detail.html"
    model = DbType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db type detail page'
        return context


class DbTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DbType
    fields = ['type', 'explain']
    template_name = 'db/db_type_update.html'
    success_url = reverse_lazy("db:db-type-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db type update page'
        return context


class DbTypeAddView(LoginRequiredMixin, CreateView):
    model = DbType
    form_class = DbTypeForm
    template_name = "db/db_type_add.html"
    success_url = reverse_lazy("db:db-type-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: db type add page'
        return context


class DbTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DbType
    fields = ['tag_name', 'tag_explain']
    template_name = 'db/db_type_delete.html'
    success_url = reverse_lazy("db:db-type-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: db type delete page'
        return context

#================================db type end==============================================


#================================db begin==============================================
class DbListView(LoginRequiredMixin, ListView):
    template_name = 'db/db_list.html'
    context_object_name = 'db_list'
    model =  MasterDb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db config page'
        return context


#================================ed end==============================================
#================================master begin==============================================

class MasterDbListView(LoginRequiredMixin, ListView):
    template_name = 'db/master_db_list.html'
    context_object_name = 'master_db_list'
    model = MasterDb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db type list page'
        return context


# class DbTypeDetailView(LoginRequiredMixin, DetailView):
#     template_name = "db/db_type_detail.html"
#     model = DbType
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title_name'] = 'iomp: db type detail page'
#         return context
#
#
class MasterDbUpdateView(LoginRequiredMixin, UpdateView):
    model = MasterDb
    fields = ['type', 'alias', 'db_port', 'status', 'open_time']
    template_name = 'db/db_type_update.html'
    success_url = reverse_lazy("db:master-db-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db type update page'
        return context


class MasterDbAddView(LoginRequiredMixin, CreateView):
    model = MasterDb
    form_class = MasterDbForm
    template_name = "db/master_db_add.html"
    success_url = reverse_lazy("db:master-db-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: master db add page'
        return context


# class DbTypeDeleteView(LoginRequiredMixin, DeleteView):
#     model = DbType
#     fields = ['tag_name', 'tag_explain']
#     template_name = 'db/db_type_delete.html'
#     success_url = '/db/db_type/list/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title_name'] = 'ioms: db type delete page'
#         return context
#================================master end==============================================
#================================salve begin==============================================

class SlaveDbListView(LoginRequiredMixin, ListView):
    template_name = 'db/slave_db_list.html'
    context_object_name = 'slave_db_list'
    model = SlaveDb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db slave db list page'
        return context


# # class DbTypeDetailView(LoginRequiredMixin, DetailView):
# #     template_name = "db/db_type_detail.html"
# #     model = DbType
# #
# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['title_name'] = 'iomp: db type detail page'
# #         return context
# #
# #
class SlaveDbUpdateView(LoginRequiredMixin, UpdateView):
    model = SlaveDb
    fields = ['alias', 'db_port', 'status', 'open_time']
    template_name = 'db/db_type_update.html'
    success_url = reverse_lazy("db:slave-db-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: db slave update page'
        return context


class SlaveDbAddView(LoginRequiredMixin, CreateView):
    model = SlaveDb
    form_class = SlaveDbForm
    template_name = "db/master_db_add.html"
    success_url = reverse_lazy("db:slave-db-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: slave db add page'
        return context


# # class DbTypeDeleteView(LoginRequiredMixin, DeleteView):
# #     model = DbType
# #     fields = ['tag_name', 'tag_explain']
# #     template_name = 'db/db_type_delete.html'
# #     success_url = '/db/db_type/list/'
# #
# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['title_name'] = 'ioms: db type delete page'
# #         return context


#================================slave end==============================================


