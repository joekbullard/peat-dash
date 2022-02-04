from peatdash.models import Grant, Site
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GrantSerializer, SiteSerializer
from django.shortcuts import redirect
from rest_framework import permissions
from peatdash.permissions import IsOwnerOrReadOnly
from django.db.models import Sum
from django.contrib.gis.db.models.functions import Area

class GrantListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'grant_list.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    area = Grant.objects.annotate(area=Sum(Area('sites__geom')))

    def get(self, request):
        queryset = Grant.objects.all()
        return Response({'grants': queryset})

    def area(self, request):
        queryset = Grant.objects.annotate(area=Sum(Area('sites__geom')))
        return Response({'area': queryset})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GrantDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'grant_detail.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    '''
    def get(self, request, pk):
        try:
            queryset = Grant.objects.get(pk=pk)
            return Response({'grant': queryset})
        except Grant.DoesNotExist:
            raise Http404
    '''
    def get(self, request, pk):
        grant = get_object_or_404(Grant, pk=pk)
        serializer = GrantSerializer(grant)
        return Response({'serializer': serializer, 'grant': grant})
    
    def post(self, request, pk):
        grant = get_object_or_404(Grant, pk=pk)
        serializer = GrantSerializer(grant, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'grant': grant})
        serializer.save()
        return redirect('grant_list')

class SiteListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'site_list.html'

    def get(self, request):
        queryset = Site.objects.all()
        return Response({'sites': queryset})

class SiteDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'site_detail.html'

    '''
    def get(self, request, pk):
        try:
            queryset = Grant.objects.get(pk=pk)
            return Response({'grant': queryset})
        except Grant.DoesNotExist:
            raise Http404
    '''
    def get(self, request, pk):
        site = get_object_or_404(Site, pk=pk)
        serializer = SiteSerializer(site)
        return Response({'serializer': serializer, 'site': site})
    
    def post(self, request, pk):
        site = get_object_or_404(Site, pk=pk)
        serializer = SiteSerializer(site, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'site': site})
        serializer.save()
        return redirect('site_list')
