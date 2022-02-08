from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point, GeometryCollection



class Neighborhoods(models.Model):
    boro_code = models.FloatField()
    boro_name = models.CharField(max_length=254)
    county_fip = models.CharField(max_length=254)
    ntacode = models.CharField(max_length=254)
    ntaname = models.CharField(max_length=254)
    shape_area = models.FloatField()
    shape_leng = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    #marker= models.MultiPointField(srid=4326, null=True)
    #gf= models.GeometryCollectionField(srid=4326, null=True)

class Marker(models.Model):
    slug= models.SlugField(null=True)
    marker= models.PointField(srid=4326)

#>>> polygon=OstanIran.objects.all().values()
#>>> poly=polygon[0]['geom'].coords


class OstanIran(models.Model):
    id_0 = models.IntegerField(null=True)
    iso = models.CharField(max_length=3, null=True)
    name_0 = models.CharField(max_length=75, null=True)
    id_1 = models.IntegerField(null=True)
    name_1 = models.CharField(max_length=75)
    varname_1 = models.CharField(max_length=150, null=True, blank=True)
    nl_name_1 = models.CharField(max_length=50, null=True, blank=True)
    hasc_1 = models.CharField(max_length=15, null=True)
    cc_1 = models.CharField(max_length=15, null=True, blank=True)
    type_1 = models.CharField(max_length=50, null=True)
    engtype_1 = models.CharField(max_length=50, null=True)
    validfr_1 = models.CharField(max_length=25, null=True)
    validto_1 = models.CharField(max_length=25, null=True)
    remarks_1 = models.CharField(max_length=125, null=True, blank=True)
    shape_leng = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326, null=True)
    
    #marker= models.GeometryCollectionField(srid=4326, default=geom.polygon)



	



