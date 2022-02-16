from django.db import models
from django.contrib.gis.db import models


# Model for entering the borders in the form of polygons
class OstanIran(models.Model):
    name = models.CharField(max_length=750)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


# Model for create marker as point
class Marker(models.Model):
    slug = models.SlugField(unique=True)
    marker = models.PointField(srid=4326)
    polygon = models.ForeignKey(OstanIran, on_delete=models.CASCADE,related_name='marker', null=True, blank=True)
    
    @property
    def polygon_name(self):
        return self.polygon.name
    @property
    def mc(self):
        coords1=self.marker.coords
        coords2=list(reversed(coords1))

        return coords2
    def __str__(self):
        return self.slug