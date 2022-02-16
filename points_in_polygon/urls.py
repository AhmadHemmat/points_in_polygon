from django.urls import path
from .views import *

name="points_in_polygon"
urlpatterns = [
    path('markers/', Markers.as_view(), name='markers'),
    path('mip/', MarkersInPolygon.as_view(), name='markers_in_polygon'),
    path('pcp/', PolygonContainsPoint.as_view(), name='polygon_contains_point'),
    path('pip/', PointsInPolygon.as_view(), name='points_in_polygon'),

    ]