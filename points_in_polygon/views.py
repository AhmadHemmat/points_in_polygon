from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.contrib.gis.geos import Point, Polygon


# View for render and send all markers
class Markers(APIView):
	def get(self, request):
		markers = Marker.objects.all().order_by('-id')
		serialized_data = MarkersSerializer(markers, many=True)
		data = serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)

# View for render and send all markers coordinates
class MarkerCoords(APIView):
	def get(self, request):
		markers = Marker.objects.all().values()
		#markers_coords = markers.marker.coords
		serialized_data = MarkersSerializer(markers, many=True)
		data = serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)


# View for rendr and extract the marker points in the one polygon
class MarkersInPolygon(APIView):
	def get(self, request):
		name = request.GET['name']
		target_polygon = get_object_or_404(OstanIran, name=name)
		markers = target_polygon.marker.all().order_by('-id')
		serialized_data = MarkersSerializer(markers, many=True)
		data = serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)

# View for render the process of Specific the Polygon Contains Point
class PolygonContainsPoint(APIView):
	def get(self, request):
		slug = request.GET['slug']
		target_marker = Marker.objects.filter(slug__contains=slug).values()
		coords = target_marker[0]['marker'].coords
		point = Point(coords)
		polygon = OstanIran.objects.filter(geom__contains=point)
		serialized_data = OstanIranSerializer(polygon, many=True)
		data = serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)

# View for rendr the process of extract the marker points in the one polygon
class PointsInPolygon(APIView):
	def get(self, request):
		name = request.GET['name']
		target_polygon = OstanIran.objects.filter(name=name).values()
		coords = target_polygon[0]['geom'].coords
		polygon = Polygon(coords[0][0])
		markers = Marker.objects.filter(marker__within=polygon).order_by('-id')
		serialized_data = MarkerSerializer(markers, many=True)
		data = serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)