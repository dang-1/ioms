#coding: utf-8
from django.shortcuts import render
#import json
#from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
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


class SiteTypeDetailView(DetailView):
    model = SiteTypeModel
    template_name = 'sitecollect/site_type_detail.html'

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
    # fields = '__all__'
    # template_name = 'sitecollect/site_type_delete.html'
    success_url = reverse_lazy("sitecollect/site_type/list/")

    # def get_queryset(self):
    #     id = self.request.id
    #     return self.model.objects.filter(id=id)
# class SiteIndex(LoginRequiredMixin, ListView):
#     template_name = 'sitecollect/index.html'
#     context_object_name = 'site_list'
#     model = SiteCollect
#
#     def get_context_data(self, **kwargs):
#         context = super(SiteIndex, self).get_context_data(**kwargs)
#         context['title_name'] = 'url page'
#         site_info = {}
#         for k in SiteCollect.objects.all():
#             if k.siteurl and k.sitename:
#                 try:
#                     site_info[k.typeid.typename].update({k.sitename: k.siteurl})
#                 except:
#                     site_info[k.typeid.typename] = {k.sitename: k.siteurl}
#         context['site_info'] =  site_info
#         return context
#
#
# class SiteAddView(ListView):
#     '''
#     ok, could use add site with type
#     '''
#     template_name = 'sitecollect/site_add.html'
#     model = SiteTypeModel
#     context_object_name = 'site_type'
#
#     def post(self, request, *args, **kwargs):
#         site_add_form = SiteForm(request.POST)
#         # print(site_add_form.cleaned_data)
#         # print(site_add_form.cleaned_data)
#         if site_add_form.is_valid():
#             print('valid site add data')
#             print(site_add_form.cleaned_data)
#             try:
#                 site_add_form.save()
#             except Exception as e:
#                 print('add fail as :{}'.format(e))
#             return HttpResponseRedirect("/sitecollect/site_add/")
#         else:
#             print("valied false")
#             return HttpResponseRedirect("/sitecollect/site_add/")
#
#         # username = login_form.cleaned_data['username']
#
#
#
#
#
# # def site_index_api(request):
# #     site_info = {}
# #     for k in SiteCollect.objects.all():
# #         if k.siteurl and k.sitename:
# #             try:
# #                 site_info[k.typeid.typename].update({k.sitename: k.siteurl})
# #             except:
# #                 site_info[k.typeid.typename] = {k.sitename: k.siteurl}
# #     #return HttpResponse(site_info, mimetype='application/json')
# #     return JsonResponse(site_info)
# #
# # def managesite(request):
# #     return render(request, 'sitecollect/manage_site.html')





#
#

#
#
# class SiteTypeNameChangeView(LoginRequiredMixin, TemplateView):
#     template_name = 'sitecollect/site_type_change.html'
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#     # def post(self, request, *args, **kwargs):
#     #     login_form = LoginForm(request.POST)  # 将数据绑定到表单
#     #     if login_form.is_valid(): #验证
#     #         username = login_form.cleaned_data['username']
#     #         password = login_form.cleaned_data['password']
#     #         print(username, password)
#     #         user = authenticate(username=username, password=password)
#     #         #if authenticate(username=username, password=password):
#     #         if user is not None:
#     #             print('exec auth')
#     #             login(request, user)
#     #             return HttpResponseRedirect("/")
#
# # def sitetypemanage(request):
# #     type_info = {}
# #     for i in SiteType.objects.all():
# #         type_info[i.typename] = i.typeid
# #
# #     return render(request, 'sitecollect/site_type_manage.html', {'site_type_list': type_info})
# #
# # def addsite(request):
# #     return render(request, 'sitecollect/add_site.html')
# #
# #
# # def deletesite(request):
# #     return render(request, 'sitecollect/delete_site.html')


