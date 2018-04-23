from django.contrib import admin
from django.contrib import admin
from hostinfo.models import server_info, HostGroup

# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname',
    'system',
    'osinfo',
    'cpu_model',
    'cpu_num',
    'memory_size',
    'createdate',
    'isdelete',
    'external_ip',
    'internal_ip1',
    'internal_ip2',]
class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['groupname']
admin.site.register(server_info, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
# Register your models here.
