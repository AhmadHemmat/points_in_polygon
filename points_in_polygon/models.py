from django.db import models
from django.contrib.gis.db import models

# Model for create marker as point
class Marker(models.Model):
    slug= models.SlugField(unique=True)
    marker= models.PointField(srid=4326)

    def __str__(self):
        return self.slug

# Model for entering the borders in the form of polygons
class OstanIran(models.Model):
    name = models.CharField(max_length=750)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name



	



