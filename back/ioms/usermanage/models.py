from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    #age = models.IntergerField(default=0)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    registTime = models.DateTimeField(max_length=250, verbose_name='join time', auto_now_add=True, blank=True)
    loginTime = models.DateTimeField(max_length=250, verbose_name='login time', auto_now=True, blank=True)

    #datetime = models.DateTimeField(auto_now_add=True)
    #phone = models.CharField(max_length=30)
    #image = models.ImageField(null=False, blank=True)

    #class Meta:
    #    verbose_name = '用户'
    #    verbose_name_plural = verbose_name
    #    ordering = ['-id']

    def __unicode__(self):
        return self.username





