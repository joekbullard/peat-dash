from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import *


class RestorationLinesSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = RestorationLines
        geo_field='geom'
        fields = '__all__'


class RestorationPointSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = RestorationPoints
        geo_field='geom'
        fields = '__all__'


class SiteSerializer(GeoFeatureModelSerializer):
    points = RestorationPointSerializer(many=True, read_only=True)
    lines = RestorationLinesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Site
        geo_field='geom'
        fields = '__all__'


class GrantSerializer(serializers.ModelSerializer):
    sites = SiteSerializer(many=True, read_only=True)
    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Grant
        geo_field ='geom'
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    grants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'grants']
    