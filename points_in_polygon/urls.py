from django.urls import path
from .views import *

urlpatterns = [
    path('pcp/', PolygonContainsPoint.as_view(), name='pcp'),
    path('pip/', PointsInPolygon.as_view(), name='pip'),
    ]