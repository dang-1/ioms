from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    outer_ip = models.CharField(max_length=50)
    inner_ip = models.CharField(max_length=50)
    osversion = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    cpu_num = models.CharField(max_length=50)
    cloudplatform = models.CharField(max_length=50)

    def __str__(self):
        return self.hostname


