#coding: utf-8
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .serializers import HostSerializer
from django.http import HttpResponse
from .models import *
from .form import HostDetailFrom

class HostIndexView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/index.html'
    context_object_name = 'host_list'
    model = Host
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(HostIndexView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: host page'
        return context

class HostDetailView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/host_detail.html'
    model = Host
    context_object_name = 'host_detail'
    pk_url_kwarg = 'host_id'

    def get_context_data(self, **kwargs):
        print(kwargs)
        # print(request.get['name'])
        context = super(HostDetailView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: host detail page'
        return context
    def get_queryset(self):
        print("id: {}".format(self.kwargs.get('pk')))
        host_detail_info = get_object_or_404(Host, pk=self.kwargs.get('pk'))
        print('info: {}'.format(host_detail_info))
        return super(HostDetailView, self).get_queryset().filter(hostname=host_detail_info)

class HostViewSet(viewsets.ModelViewSet):
    '''
    api
    '''
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/project_list.html'
    context_object_name = 'project_list'
    model = ProjectName
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: host project page'
        return context




class CloudPlatView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/platfrom_list.html'
    context_object_name = 'cloudplat_list'
    model = CloudPlat
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(CloudPlatView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: host platfrom page'
        return context

class RoleView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/role_list.html'
    context_object_name = 'role_list'
    model = HostRole
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(RoleView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: host role page'
        return context


class StatusView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/status_list.html'
    context_object_name = 'status_list'
    model = HostStatus

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        context['title_name'] = 'iomp: host status page'
        return context

class HostStatusDetailView(DetailView):
    model = HostStatus
    template_name = 'hostmanage/host_status_detail.html'


def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file', None)
        if upload_file is None:
            return HttpResponse('No file get')
        else:
            with open('/tmp/{}'.format(upload_file.name), 'wb') as f:
                f.write(upload_file.read())
            return HttpResponse('Ok')
    else:
        return render(request, 'hostmanage/upload_file.html')

