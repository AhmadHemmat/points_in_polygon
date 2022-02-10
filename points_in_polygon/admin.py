from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

# use LeafletGeoAdmin api for map infrastructure in admin panel
class PointsInPolygonAdmin(LeafletGeoAdmin):
	pass
	
# add Marker and OstanIran models to admin panel
admin.site.register(OstanIran, PointsInPolygonAdmin)
admin.site.register(Marker, PointsInPolygonAdmin)
