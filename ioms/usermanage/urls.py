from usermanage.views import *
from django.conf.urls import include, url
#from django.contrib import admin


urlpatterns = [
    url(r'^index/', usermanage_index),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', index),
    #url(r'^register$', register_view),
    #url(r'^login$', login_view),
    #url(r'^logout$', logout_view)
]