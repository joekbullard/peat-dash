from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from .models import *

class SiteInLine(LeafletGeoAdminMixin, admin.StackedInline):
    model = Site
    extra=0
    readonly_fields = ('name',)

class GrantReferenceAdmin(admin.ModelAdmin):
    inlines = [
        SiteInLine,
    ]

admin.site.register(Grant, GrantReferenceAdmin)
admin.site.register(Site, LeafletGeoAdmin)
admin.site.register(RestorationLines, LeafletGeoAdmin)
admin.site.register(RestorationPoints, LeafletGeoAdmin)
