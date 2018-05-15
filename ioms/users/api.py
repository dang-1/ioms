#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 上午9:36
# @Author  : tang
# @FileName: api.py
# @Software: PyCharm
# @Mail    : 93651849@qq.com

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets, routers
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets, generics
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


    # def get_object(self, pk):
    #     try:
    #         return User.objects.get(pk=pk)
    #     except:
    #         pass
# class UserViewSet2(APIView):
#     def get(self, request, format=None):
#         usernames = [user.name for user in User.objects.all()]
#         return Response(usernames)



