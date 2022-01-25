from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *

admin.site.register(GrantReference)
admin.site.register(SiteOutline, LeafletGeoAdmin)
admin.site.register(RestorationLines, LeafletGeoAdmin)
admin.site.register(RestorationPoints, LeafletGeoAdmin)
