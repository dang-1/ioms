#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 下午4:47
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets, routers

from .serializers import HostSerializer, HostRoleSerializer, ProjectNameSerializer, CloudPlatSerializer, HostStatusSerializer
from .models import Host, HostRole, ProjectName, CloudPlat, HostStatus

class RoleView(viewsets.ModelViewSet):
    queryset = HostRole.objects.all().order_by('id')
    serializer_class = HostRoleSerializer


class ProjectNameView(viewsets.ModelViewSet):
    queryset = ProjectName.objects.all().order_by('id')
    serializer_class = ProjectNameSerializer


class CloudPlatView(viewsets.ModelViewSet):
    queryset = CloudPlat.objects.all().order_by('id')
    serializer_class = CloudPlatSerializer


class HostStatusView(viewsets.ModelViewSet):
    queryset = HostStatus.objects.all().order_by('id')
    serializer_class = HostStatusSerializer


class HostView(viewsets.ModelViewSet):
    '''
    api
    '''
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    paginate_by = 20
    page_size = 15




# class HostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Host.objects.all()
#     serializer_class = HostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# class HostView(generics.ListCreateAPIView):
#     queryset = Host.objects.all()
#     serializer_class = HostSerializer


# class HostDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Host.objects.all()
#     serializer_class = HostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# class HostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Host.objects.all()
#     serializer_class = HostSerializer


# from .serializers import UserSerializer
# from .models import User
# from rest_framework import viewsets, generics
# # class UserInfoListView(APIView):
# #     def get(self, request, format=None):
# #         users = User.objects.all()
# #         serializer = UserSerializer(users, many=True)
# #         return Response(serializer.data)
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('username')
#     serializer_class = UserSerializer
#     # paginate_by = 3
#
#
# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()

