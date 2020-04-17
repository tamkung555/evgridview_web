from django.shortcuts import render
from .models import Transformer_PBA, Transformer_C2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def index(request): # function to response dashboard index page
    
    # qs = Transformer_C2.objects.all().values().filter(facilityid="49-005910")
    # qs = Transformer_C2.objects.all().values()
    return render(request, 'map.html', {"data": None})

def dashboard(request):
    return render(request, 'home.html')

@csrf_exempt
def search_by_peano(request): # TODO : re-develope function to handle request from Outside Services.
    """
        change function to handle update request, return only response
        
    """
    if request.method == "POST":
        
        peano = request.POST.get('peano') 
        print(peano)
        qs = Transformer_C2.objects.filter(facilityid__contains=peano)
        res = []
        for i in qs.values():
            res.append({"peano": i.get("facilityid"), "flag": i.get("flag"),
                        "impact": i.get("impact"), "numberOfCustomer" : i.get("numberOfCustomer")})
        
        print(res)
    # return render(request, 'result.html', {"data": list(qs)})
    return JsonResponse({"data": res})

@csrf_exempt
def update_attribute_transformer(request):
    if request.method == "POST":
        peano = request.POST.get("peano")
        flag = True
        impact = json.loads(request.POST.get("impact"))
        loadProfile_base = json.loads(request.POST.get("loadprofile_base"))
        loadProfile_ev = json.loads(request.POST.get("loadprofile_ev"))
        number_of_meter = request.POST.get("number_of_customer")
        
        # print(loadProfile_base)
        # print(type(loadProfile_base))
        
        # --
        print("PEANO :{}".format(peano))
        qs = Transformer_C2.objects.filter(facilityid__contains=peano)
        # for item in qs.values():
        #     item.update(flag=True, impact=impact,
        #                 loadProfile_base=loadProfile_base ,
        #                 loadProfile_ev=loadProfile_ev,
        #                 numberOfCustomer=number_of_meter)
            
        for obj in qs:
            obj.flag = True
            obj.impact = impact
            obj.loadProfile_base=loadProfile_base
            obj.loadProfile_ev=loadProfile_ev
            obj.numberOfCustomer=number_of_meter
            obj.save()
            
            
    return JsonResponse({"Status": "Updated"})
        
    
    

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