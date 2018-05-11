#coding: utf-8
from django.shortcuts import render
#import json
#from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from .serializers import SiteTypeSerializer
from .models import SiteTypeModel, SiteCollectModel
from .form import  SiteForm, SiteTypeForm


class SiteTypeListView(LoginRequiredMixin, ListView):
    template_name = 'sitecollect/site_type_list.html'
    context_object_name = 'site_type'
    model = SiteTypeModel

    def get_context_data(self, **kwargs):
        context = super(SiteTypeListView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: url type page'
        return context


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


class SiteTypeApiView(APIView):
    def get(self, request, fromat=None):
        site_type = SiteTypeModel.objects.all()
        serailizer = SiteTypeSerializer(site_type, many=True)

        return JsonResponse(serailizer.data)
    # queryset = SiteTypeModel.objects.all().order_by('id')
    # serializer_class = SiteTypeSerializer

class SiteTypeDetailView(DetailView):
    model = SiteTypeModel
    template_name = 'sitecollect/site_type_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SiteTypeListView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: url type detail page'
        return context

    # def get_queryset(self, pk=1):
    #     return SiteType.object.get(id=pk)
    # form_class = SiteTypeForm
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     return context

class SiteTypeAddView(LoginRequiredMixin, CreateView):
    model = SiteTypeModel
    form_class = SiteTypeForm
    template_name = 'sitecollect/site_type_add.html'
    success_url = '/sitecollect/site_type/list'

    def get_context_data(self, **kwargs):
        context = super(SiteTypeAddView, self).get_context_data(**kwargs)
        context['title_name'] = 'site type add page'
        return context


class SiteTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = SiteTypeModel
    # form_class = SiteTypeForm
    fields = ['site_type_name']
    template_name = 'sitecollect/site_type_update.html'
    # template_name_suffix = '_update_form'
    # fields = ['typename']
    success_url = '/sitecollect/site_type/list'

    # def form_invalid(self, form):
    #     return HttpResponseRedirect("/sitecollect/site_type_list/")



class SiteTypeModelDeleteView(LoginRequiredMixin, DeleteView):
    models = SiteTypeModel
    fields = ['id', 'site_type_name']
    template_name = 'sitecollect/site_type_delete.html'
    success_url = '/sitecollect/site_type/list'

    def get_queryset(self):
        data = SiteTypeModel.objects.filter(id=self.kwargs['pk'])
        return data

    # def get_queryset(self):
    #     # return get_object_or_404(SiteTypeModel, id=self.kwargs['pk'])
    #     return SiteTypeModel.objects.get(id=self.kwargs['pk'])
        # xxxxx = get_object_or_404(SiteTypeModel, id=self.kwargs['pk'])
        # print(xxxxx)
        # return xxxxx

class SiteListView(LoginRequiredMixin, ListView):
    template_name = 'sitecollect/site_list.html'
    context_object_name = 'type_list'
    model = SiteTypeModel

    def get_context_data(self, **kwargs):
        context = super(SiteListView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: url list page'
        return context


class SiteManageView(LoginRequiredMixin, ListView):
    template_name = 'sitecollect/site_manage.html'
    context_object_name = 'site_list'
    model = SiteCollectModel
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(SiteManageView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: url manage page'
        return context


class SiteAddView(LoginRequiredMixin, CreateView):
    model = SiteTypeModel
    form_class = SiteForm
    template_name = 'sitecollect/site_add.html'
    success_url = '/sitecollect/site/list'

    def get_context_data(self, **kwargs):
        context = super(SiteAddView, self).get_context_data(**kwargs)
        context['title_name'] = 'site add page'
        return context


class SiteDetailView(DetailView):
    model = SiteCollectModel
    template_name = 'sitecollect/site_detail.html'


class SiteUpdateView(LoginRequiredMixin, UpdateView):
    model = SiteCollectModel
    # form_class = SiteTypeForm
    fields = ['sitename', 'siteurl', 'typeid']
    template_name = 'sitecollect/site_update.html'
    success_url = '/sitecollect/site/list'


class SiteDeleteView(DeleteView):
    models = SiteCollectModel
    fields = ['siteurl', 'sitename']
    template_name = 'sitecollect/site_delete.html'
    success_url = '/sitecollect/site/list/'

    def get_queryset(self):
        data = SiteCollectModel.objects.filter(id=self.kwargs['pk'])
        return data

