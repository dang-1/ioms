#coding: utf-8

from rest_framework import serializers

from .models import Host

class HostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Host
		fields = ('outer_ip', 'inner_ip')





