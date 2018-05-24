#coding: utf-8
import json
import requests

from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .serializers import HostSerializer
from .form import HostFrom, HostRoleForm, PorjectFrom

def update_host_view(request):
    # error_info = {}
    iop_host_api_url = "https://iop-api.tap4fun.com/real_servers/unsecure_list?"
    #identifier
    get_total_info = json.loads(requests.get(iop_host_api_url).text)
    total_page = int(get_total_info["total_pages"]) #ok
    for i in range(1, total_page+1):
        page_url_api = "{}page={}".format(iop_host_api_url, i)
        hosts_data = json.loads(requests.get(page_url_api).text)['data']
        for j in range(len(hosts_data)):
            host_data = hosts_data[j]
            # try:
            instance_id = host_data.get('identifier', '')
            public_ip = ','.join(host_data.get("public_ip_addresses"))
            private_ip = ','.join(host_data.get('private_ip_addresses'))
            hostname = host_data.get('hostname', '')
            project = host_data.get("project").get('bastion_group_name', '')
            # role = None if not host_data.get('tags').get('roles') else ','.join(host_data.get('tags').get('roles'))
            role = host_data.get('tags').get('roles')
            # print('{} {} {} {} {} {}'.format(instance_id, public_ip, private_ip, hostname, project, role))
            # print('{} {} {} {} {} {}'.format(type(instance_id), type(public_ip), type(private_ip), type(hostname),
            #                                      type(project), type(role)))
            # print(role)
            if role:
                for role_one in role:
                    print(role_one)
                    try:
                        a = HostRole.objects.get(role=role_one)
                    except:
                        r = HostRoleForm({'role': role_one})
                        if r.is_valid():
                            print('valid')
                            r.save()
                        else:
                            print('save error')
                            # r = HostRole.objects.get(role=i)
            if project:
                try:
                    pro = ProjectName.objects.get(project_name=project)
                except:
                    p = PorjectFrom({'project_name':project})
                    if p.is_valid():
                        p.save()
                    else:
                        print('save pro error')
            pro = ProjectName.objects.get(project_name=project)
            print(1)
            try:
                h = Host(
                    instance_id=instance_id,
                    outer_ip=public_ip,
                    inner_ip=private_ip,
                    hostname=hostname
                )
                h.save()
                print(2)
            except Exception as e:
                print('save {} error as {}'.format(instance_id, e))
            if role:
                print(role)
                for r in role:
                    h.role.add(HostRole.objects.get(role=r))
                # h.role.set = (HostRole.objects.get(role=ro) for ro in role)
                # h.save()
                # host_info = HostForm({
                #     # 'instance_id': host_data.get('identifier', 'xxx'),
                #     # 'public_ip': ','.join(host_data.get("public_ip_addresses", 'xxx')),
                #     # 'private_ip': ','.join(host_data.get('private_ip_addresses', 'xxx')),
                #     # 'hostname': host_data.get('hostname', 'xxx'),
                #     # 'project': host_data.get("project").get('bastion_group_name', 'xxx'),
                #     # 'role': ','.join(host_data.get('tags').get('roles', 'xxx'))}
                #     'instance_id': host_data.get('identifier'),
                #     'public_ip': ','.join(host_data.get("public_ip_addresses")),
                #     'private_ip': ','.join(host_data.get('private_ip_addresses')),
                #     'hostname': host_data.get('hostname'),
                #     'project': host_data.get("project").get('bastion_group_name'),
                #     'role': None if not host_data.get('tags').get('roles') else ','.join(host_data.get('tags').get('roles'))}
                # )
            # except Exception as e:
            print('save {} ok in page: {} {}'.format(instance_id, j, i))
                # continue

            # if host_info.is_valid():
            #     host_info.save()
            # else:
            #     print('save eror')
    return redirect('/hostmanage/host_index/')



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


class HostStatusView(LoginRequiredMixin, ListView):
    template_name = 'hostmanage/status_list.html'
    context_object_name = 'status_list'
    model = HostStatus

    def get_context_data(self, **kwargs):
        context = super(HostStatusView, self).get_context_data(**kwargs)
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

