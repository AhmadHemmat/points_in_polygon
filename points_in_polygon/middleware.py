from .models import *
from django.contrib.gis.geos import Point


# this middleware fill the polygon field of Marker model(Specific the Polygon Contains Point)
class SavePolygonMarkerMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		markers=Marker.objects.all()
		for x in markers:
			marker=Marker.objects.all()[0]
			coords=marker.marker.coords
			point=Point(coords)
			polygon=OstanIran.objects.filter(geom__contains=point)[0]
			marker_polygon= polygon
			marker.polygon=marker_polygon
			marker.save()
		response = self.get_response(request)
		return response