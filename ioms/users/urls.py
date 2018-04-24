# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2018/4/8 下午1:59
# # @Author  : tang
# # @FileName: urls.py
# # @Software: PyCharm
# # @Mail    : 93651849@qq.com

# from .views import Login, user_logout, UserList, UserAdd, register, test_page


# urlpatterns = [
#     #url(r'^login/$', login, name='login'),
#     url(r'^login/$', Login.as_view(), name='login'),
#     url(r'^register/$', register, name='register'),
#     url(r'^logout/$', user_logout, name='logout'),
#     #url(r'^index/api/$', site_index_api, name='siteindexapi'),
#     url(r'^user_list', UserList.as_view(), name='user_list'),
#     url(r'^useradd', UserAdd.as_view(), name='user_add'),
#     url(r'^test_page', test_page, name='test_page')
#     #url(r'^addsite', addsite, name='addsite'),
#     #url(r'^deletesite', deletesite, name='deletesite'),

# ]
from django.contrib import admin
from django.urls import path

from .views import Login, user_logout, UserAdd, UserList

app_name = 'users'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'), #ok
    path('logout/', user_logout, name='logout'),
    path('register/', Login.as_view(), name='register'),
    # path('user_list/', Login.as_view(), name='user_list'),
    path('user_add/', UserAdd.as_view(), name='user_add'),
    path('user_list/', UserList.as_view(), name='user_list'),
    # path('login/$', )
]