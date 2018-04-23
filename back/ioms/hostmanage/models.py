from django.db import models

# Create your models here.
class server_info(models.Model):
    '''store new host information'''
    hostname = models.CharField(max_length=200)
    system = models.CharField(max_length=20)
    osinfo = models.CharField(max_length=200)
    cpu_model = models.CharField(max_length=200)
    cpu_num = models.CharField(db_column='CPU', max_length=20)
    memory_size = models.CharField(max_length=20)
    #createdate = models.DateField(max_length=255,auto_now_add=True,default=datetime.datetime.now().strftime("%Y-%m-%d"),null=True)
    createdate = models.CharField(max_length=200)
    isdelete = models.IntegerField(default=0,null=True)
    external_ip = models.IPAddressField(max_length=20)
    internal_ip1 = models.IPAddressField(db_column='internalip1', max_length=20)
    internal_ip2 = models.IPAddressField(db_column='internalip2', max_length=20, null=True)
    def __unicode__(self):
        return self.internal_ip1
class HostGroup(models.Model):
    groupname = models.CharField(max_length=50)
    members = models.ManyToManyField(server_info)



