"""API Control serializers."""
from rest_framework import serializers
from .models import (
    App,
    OrganizationalUnitType,
    OrganizationalUnit
)


class OrganizationalUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationalUnit
        fields = ('name', 'description', 'unit_type',
                  'created_at', 'updated_at')


class OrganizationalUnitTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationalUnitType
        fields = ('name', 'description', 'app', 'parent', 'units')
        read_only_fields = ('units',)


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
