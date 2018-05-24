#coding: utf-8

from rest_framework import serializers

from .models import Host, HostRole


class HostRoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = HostRole
		fields = ('role',)


# class HostSerializer(serializers.HyperlinkedModelSerializer):
class HostSerializer(serializers.ModelSerializer):
	# roles = HostRoleSerializer(many=True, read_only=True)
	# host_role = serializers.SlugRelatedField(many=True, slug_field='role')
	class Meta:
		model = Host
		fields = (
			'id',
			'hostname',
			'status',
			'outer_ip',
			'inner_ip',
			'osversion',
			'role',
			# 'host_role',
		)
		read_only_fields = ('id',)
		depth = 1


