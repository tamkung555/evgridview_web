from django.shortcuts import render
from .models import Transformer_PBA, Transformer_C2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def index(request): # function to response dashboard index page
    
    # qs = Transformer_C2.objects.all().values().filter(facilityid="49-005910")
    # qs = Transformer_C2.objects.all().values()
    return render(request, 'map.html', {"data": None})

@csrf_exempt
def search_by_peano(request): # TODO : re-develope function to handle request from Outside Services.
    """
        change function to handle update request, return only response
        
    """
    if request.method == "POST":
        
        peano = request.POST.get('peano') 
        qs = Transformer_PBA.objects.filter(facilityid__contains=peano)
        res = []
        for i in qs.values():
            i.update(flag=True, impact=['green']) # TODO :review impact field and consideration to add loadProfile field.
            res.append({"peano": i.get('facilityid'), \
                        "coordinate": [i.get('lat'), i.get('long')], \
                        "flag": i.get('flag'), \
                        "impact": i.get("impact")})
            
        for obj in qs:
            obj.flag = True
            obj.save()
        
    # return render(request, 'result.html', {"data": list(qs)})
    return JsonResponse({"data": res})


def count_by_flag(request): # Function for Count object that analysised
    qs = Transformer_PBA.objects.all().values().filter(flag=True)
    res = []
    for i in qs:
        print(i)
        res.append({"peano": i.get('facilityid'), "coordinate": [i.get('lat'), i.get('long')], "flag": i.get('flag'), "impact": i.get("impact")})
        
    # return render(request, 'result.html', {"data": list(qs)})
    return JsonResponse({"data": res, "count": len(qs)})


@csrf_exempt
def map_request(request): # Search by Attribute
    print("Hello JS")
    # bbox = request.POST.get('bbox', "NO KEY")
    # print(bbox)
    print("------------- >")
    print(request.POST)
    print("------------- >")
    peano = request.POST.get('data')
    print(peano)
    qs = Transformer_C2.objects.all().values().filter(facilityid=peano)
    res = []
    
    for i in qs:
        # print(i.get('facilityid'), [i.get('lat'), i.get('long')])
        res.append({"peano": i.get('facilityid'), "coordinate": [i.get('lat'), i.get('long')]})
        print("---- > < ----")
        print(res)
        
    return JsonResponse({"data": res})

@csrf_exempt
def map_query_extend(request):
    bbox = json.loads(request.GET["extend"])
    print(bbox)
    print(type(bbox))
    # res = request.POST.get("extend")
    return JsonResponse({"data": "200 OK"})