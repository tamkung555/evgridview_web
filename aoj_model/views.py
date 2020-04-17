from django.shortcuts import render
from .models import Aoj_C2
from transformer_model.models import Transformer_C2

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.contrib.gis.db.models.functions import AsGeoJSON, Centroid

from django.contrib.gis.gdal import DataSource
import transformer_model
import os

@csrf_exempt
def select_aoj_request(request): # function for select by location and send data to map
    
    aoj_code = json.loads(request.GET["code"]) # get AOJ code from html 
    aoj = Aoj_C2.objects.all().filter(code=aoj_code) # AOJ queryset from Models
    aoj_poly = aoj[0].geom # aoj_poly is Geometry Dataset 
    tr = Transformer_C2.objects.all().filter(geom__within = aoj_poly) # Transformer in AOJ Polygon
    
    # built AOJ GeoJSON object and add centroid in fields cent.
    qs = Aoj_C2.objects.all().filter(code=aoj_code).annotate(cent=AsGeoJSON(Centroid('geom')))
    for i in qs.values():
        print(json.loads(i.get("cent")).get("coordinates"))
        centroid_aoj = json.loads(i.get("cent")).get("coordinates")
    
    res = serialize( # pack GeoJSON in res variable.
        'geojson',
        Aoj_C2.objects.all().filter(code=aoj_code),
        fields=('geom', ),
    )
    
    tr_geojson = serialize(
        'geojson',
        Transformer_C2.objects.all().filter(geom__within = aoj_poly),
        fields=('geom', ),
    )
  
    result = []
    result_dict = {}
    for i in tr :
       
        json_obj = json.loads(i.geom.json)
        # Edit JSON Schema if you want addition more fields.
        result_dict.update({"peano": i.facilityid, "ratekva": i.ratekva, 
                            "gistag" : i.tag, "feederID": i.feederid, "phase" : i.phasedesig,
                            "name" : i.name, "flag" : i.flag,
                            "impact" : i.impact, "baseload" : i.loadProfile_base,
                            "numberOfCustomer" : i.numberOfCustomer,
                            "evload" : i.loadProfile_ev, "coordinate": json_obj["coordinates"]})
        
     
        result.append(result_dict)
        result_dict = {}
        
    # data = json.loads(tr_geojson)
    # with open("./transformer_geojson.json", 'w') as f:
    #     json.dump(data, f)
    
    return JsonResponse({
                         "data": res, \
                         "coordinate_cent" : centroid_aoj, \
                         "point": json.dumps(result)
                         
                         })
    