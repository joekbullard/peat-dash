from django.urls import path
from .views import GrantListView, GrantDetailView, SiteListView, SiteDetailView
from .viewsets import GrantViewSet

urlpatterns = [
    path('', GrantListView.as_view(), name='grant_list'),
    path('<int:pk>/', GrantDetailView.as_view(), name='grant_detail'),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site_detail'),
    path('sites/', SiteListView.as_view(), name='site_list'),
]