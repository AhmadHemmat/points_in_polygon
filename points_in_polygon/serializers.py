from rest_framework import serializers
from .models import *


# serializer of Markers model for use in Markers and MarkersInPolygon views
class MarkersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marker
        fields = ['marker', 'slug', 'polygon_name' ]

# serializer of OstanIran model for use in PolygonContainsPoint view
class OstanIranSerializer(serializers.ModelSerializer):
    class Meta:
        model = OstanIran
        fields = ['name', ]

# serializer of Marker model for use in PointsInPolygon view
class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['marker', 'slug' ]