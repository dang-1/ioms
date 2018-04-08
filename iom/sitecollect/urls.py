from django.conf.urls import url

from .views import *



urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^hostmanage', include('hostmanage.urls')),
    url(r'^index/$', siteindex, name='siteindex'),
    url(r'^index2/$', siteindex2.as_view(), name='siteindex2'),
    url(r'^index/api/$', site_index_api, name='siteindexapi'),
    url(r'^managesite', managesite, name='managesite'),
    url(r'^sitetypemanage', sitetypemanage, name='typemanage'),
    url(r'^addsite', addsite, name='addsite'),
    url(r'^deletesite', deletesite, name='deletesite'),

]