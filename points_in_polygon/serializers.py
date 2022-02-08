from rest_framework import serializers
from .models import *


class SingleArticleSerializer(serializers.Serializer):
    name_1 = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
   

class OstanIranSerializer(serializers.ModelSerializer):
    class Meta:
        model = OstanIran
        fields = ['name_1', ]


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['marker', 'slug' ]