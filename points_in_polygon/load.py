import os
from django.contrib.gis.utils import LayerMapping
from .models import *

# Auto-generated `LayerMapping` dictionary for Neighborhood model
neighborhood_mapping = {
    'boro_code': 'boro_code',
    'boro_name': 'boro_name',
    'county_fip': 'county_fip',
    'ntacode': 'ntacode',
    'ntaname': 'ntaname',
    'shape_area': 'shape_area',
    'shape_leng': 'shape_leng',
    'geom': 'MULTIPOLYGON',
}


neighborhood_shapefile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'NTA/geo_export_a7bcba49-5e0a-45fd-bda0-1eec0391ce3e.shp')) 

def run(verbose=True):
    layermap = LayerMapping(Neighborhoods,neighborhood_shapefile,neighborhood_mapping,transform=False, encoding='iso-8859-1')
    layermap.save(strict=True,verbose=verbose)