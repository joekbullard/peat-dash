from rest_framework import viewsets
from rest_framework_gis import filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import GrantSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class GrantViewSet(viewsets.ModelViewSet):
    
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer


    def list(self, request):
        queryset = Grant.objects.all()
        serializer = GrantSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Grant.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = GrantSerializer(user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)