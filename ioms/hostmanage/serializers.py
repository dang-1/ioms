#coding: utf-8

from rest_framework import serializers

from .models import Host, HostRole, ProjectName, CloudPlat


class HostRoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = HostRole
		fields = ('role',)


class ProjectNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectName
		fields = ('id', 'project_name')


class CloudPlatSerializer(serializers.ModelSerializer):
	class Meta:
		model = CloudPlat
		fields = ('id', 'provider', 'cloud_platform_name', 'locate', 'city')


# class HostSerializer(serializers.HyperlinkedModelSerializer):
class HostSerializer(serializers.ModelSerializer):
	role_display = serializers.SerializerMethodField()
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
			'role_display',
		)
		read_only_fields = ('id',)
		depth = 1
	@staticmethod
	def get_role_display(obj):
		return ",".join([x.role for x in obj.role.all()])


