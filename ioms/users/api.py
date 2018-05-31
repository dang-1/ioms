#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 上午9:36
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
# from common.utils import reverse, get_object_or_none
from rest_framework import viewsets, generics
from .serializers import UserSerializer, GroupSerializer
from .models import User, UserGroup
from rest_framework_bulk import BulkModelViewSet, ListBulkCreateUpdateDestroyAPIView

# class UserViewSet(BulkModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_fields = ('username', 'email', 'name', 'id')

# class UserView(ListBulkCreateUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserInfoListView(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    # paginate_by = 3


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

class GroupView(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all().order_by('name')
    serializer_class = GroupSerializer
    # def get_object(self, pk):
    #     try:
    #         return User.objects.get(pk=pk)
    #     except:
    #         pass
# class UserViewSet2(APIView):
#     def get(self, request, format=None):
#         usernames = [user.name for user in User.objects.all()]
#         return Response(usernames)



