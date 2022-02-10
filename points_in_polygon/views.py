from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.contrib.gis.geos import Point, Polygon


# View for render and send all markers
class Markers(APIView):
	def get(self, format=None):
		markers=Marker.objects.all().order_by('-id')
		serialized_data=MarkersSerializer(markers, many=True)
		data=serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)

# View for rendr and extract the marker points in the one polygon
class MarkersInPolygon(APIView):
	def get(self, request, format=None):
		name=request.GET['name']
		polygon=get_object_or_404(OstanIran, name=name)
		markers=polygon.marker.all()
		serialized_data=MarkersSerializer(markers, many=True)
		data=serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)

# View for render the process of Specific the Polygon Contains Point
class PolygonContainsPoint(APIView):
	def get(self, request, format=None):
		marker_slug=request.GET['slug']
		marker2=Marker.objects.filter(slug__contains=marker_slug).values()
		m=marker2[0]['marker'].coords
		p=Point(m)
		polygon=OstanIran.objects.filter(geom__contains=p)
		serialized_data=OstanIranSerializer(polygon, many=True)
		data=serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)

# View for rendr the process of extract the marker points in the one polygon
class PointsInPolygon(APIView):
	def get(self, request, format=None):
		name=request.GET['name']
		polygon=OstanIran.objects.filter(name__contains=name).values()
		poly=polygon[0]['geom'].coords
		p=Polygon(poly[0][0])
		marker=Marker.objects.filter(marker__within=p)
		serialized_data=MarkerSerializer(marker, many=True)
		data=serialized_data.data
		return Response({'data': data}, status=status.HTTP_200_OK)