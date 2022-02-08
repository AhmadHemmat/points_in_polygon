from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.gis.geos import Point, Polygon


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

class PointsInPolygon(APIView):
	def get(self, request, format=None):
		name_1=request.GET['name_1']
		polygon=OstanIran.objects.filter(name_1__contains=name_1).values()
		poly=polygon[0]['geom'].coords
		p=Polygon(poly[0][0])
		marker=Marker.objects.filter(marker__within=p)
		serialized_data=MarkerSerializer(marker, many=True)
		data=serialized_data.data

		return Response({'data': data}, status=status.HTTP_200_OK)

	

#class PointsInPolygon(viewsets.ModelViewSet):
#	ostan= OstanIran.objects.all().values()
#	i2=0
#	for y in ostan:
#		poly=ostan[i2]['geom'].coords
#		polygon=Polygon(poly[0][0])
#		queryset=Marker.objects.filter(marker__within=polygon)
#		i2=i2+1
#		serializer_class=MarkerSerializer
		
