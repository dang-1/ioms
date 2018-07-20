from django.db import models

# Create your models here.


__all__ = ['MaintenanceStatusModel', 'MaintenanceModel']


class MaintenanceStatusModel(models.Model):
    '''
    status
    '''
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=48, null=False, blank=False, verbose_name='状态')



class MaintenanceModel(models.Model):
    '''
    maintenance example
    '''
    id = models.AutoField(primary_key=True)
    ips = models.CharField(max_length=128, null=True, verbose_name='ip列表')
    maintenance_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='维护事件名称')
    start_time = models.CharField(max_length=128, verbose_name='维护开始时间')
    end_time = models.CharField(max_length=128, verbose_name='维护结束时间')
    status = models.ForeignKey(MaintenanceStatusModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="状态")






