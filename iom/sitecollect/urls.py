from django.conf.urls import url

from .views import *



urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^hostmanage', include('hostmanage.urls')),
    url(r'^index', siteindex, name='siteindex'),
    url(r'^managesite', managesite, name='managesite'),
    url(r'^sitetypemanage', sitetypemanage, name='typemanage'),
    url(r'^addsite', addsite, name='addsite'),
    url(r'^deletesite', deletesite, name='deletesite'),

]