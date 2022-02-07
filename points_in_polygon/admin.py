from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin


class PointsInPolygonAdmin(LeafletGeoAdmin):
	pass

#admin.site.register(PointsInPolygon, PointsInPolygonAdmin)
admin.site.register(Neighborhoods, PointsInPolygonAdmin)
admin.site.register(OstanIran, PointsInPolygonAdmin)
admin.site.register(Marker, PointsInPolygonAdmin)