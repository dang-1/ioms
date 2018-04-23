#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from hostinfo.models import server_info,HostGroup
import json


# Create your views here.
def collect(req):
    if req.POST:
        obj = json.loads(req.body)
        print obj
        hostname = obj['hostname']
        system = obj['system']
        osinfo = obj['osinfo']
        cpu_model = obj['cpu_model']
        cpu_num = obj['cpu_num']
        memory_size = obj['memory_size']
        createdate = obj['createdate']
        isdelete = obj['isdelete']
        external_ip = obj['external_ip']
        internal_ip1 = obj['internal_ip1']
        internal_ip2 = obj['internal_ip2']
        #try:
        #    serverinfo = server_info.objects.get(internal_ip1=internal_ip1)
        #except:
        #    serverinfo = server_info()
        serverinfo = server_info()
        serverinfo.hostname = hostname
        serverinfo.system = system
        serverinfo.osinfo = osinfo
        serverinfo.cpu_model = cpu_model
        serverinfo.cpu_num = cpu_num
        serverinfo.memory_size = memory_size
        serverinfo.createdate = createdate
        serverinfo.isdelete = isdelete
        serverinfo.external_ip = external_ip
        serverinfo.internal_ip1 = internal_ip1
        serverinfo.internal_ip2 = internal_ip2
        serverinfo.save()
        return HttpResponse('insert ok')
    else:
        return HttpResponse('no data')
def getjson(req):
    ret_list = []
    hg = HostGroup.objects.all()
    for g in hg:
        ret = {'grouname':g.groupname,'members':[]}
        for h in g.members.all():
            ret_h = {'hostname':h.hostname,'ip':h.ip}
            ret['members'].append(ret_h)
        ret_list.append(ret)
    return HttpResponse(json.dumps(ret_list))
def gettxt(req):
    res = ''
    hg = HostGroup.objects.all()
    for g in hg:
        groupname = g.groupname
        for h in g.members.all():
            hostname = h.hostname
            ip = h.ip
            res += groupname+' '+hostname+' '+ip+'\n'
    return HttpResponse(res)

