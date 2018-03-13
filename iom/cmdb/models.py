from django.db import models

# Create your models here.

class ke(models.Model):
    hostname = models.CharField(max_length=50)
    hostip = models.CharField(max_length=50)
    gs_zone = models.CharField(max_length=50) #gs/throne/tango/
    gs_alias = models.CharField(max_length=50) #game alias
    gs_accelerate_port = models.CharField(max_length=50) #accelerate port
    gs_dir = models.CharField(max_length=50)
    gs_name = models.CharField(max_length=50)
    gs_db_outer_ip = models.CharField(max_length=50)
    gs_db_inner_ip = models.CharField(max_length=50)
    gs_status = models.CharField(max_length=50)
    gs_open_time = models.CharField(max_length=50)
    gs_branch = models.CharField(max_length=50)
    gs_branch_commit_id = models.CharField(max_length=50)
    gs_merged = models.CharField(max_length=50)
    gs_merged_time = models.CharField(max_length=50)
    gs_merged_to = models.CharField(max_length=50)

    def __str__(self):
        return self.gs_name








