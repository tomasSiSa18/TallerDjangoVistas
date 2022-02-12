from django.shortcuts import render

from measurements.models import Measurement
from .logic import measurments_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurments_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurment_dto = ml.get_measurment(id)
            measurment = serializers.serialize('json', [measurment_dto,])
            return HttpResponse(measurment, 'application/json')
        else:
            measurments_dto = ml.get_measurments()
            measurments = serializers.serialize('json', measurments_dto)
            return HttpResponse(measurments, 'application/json')
    if request.method == 'POST':
        measurment_dto = ml.create_measurment(json.loads(request.body))
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

@csrf_exempt
def measurment_view(request, pk):
    if request.method == 'GET':
        measurment_dto = ml.get_measurment(pk)
        print(type(measurment_dto))
        measurment = serializers.serialize('json', [measurment_dto,])
        return HttpResponse(measurment, 'application/json')

    elif request.method == 'PUT':
        measurment_dto = ml.update_measurment(pk, json.loads(request.body))
        print(type(measurment_dto))
        measurment = serializers.serialize('json', [measurment_dto])
        return HttpResponse(measurment, 'application/json')
    elif request.method == 'DELETE':
        print("Pero aqui tambiennnnnnn")
        deleted_measurment = ml.delete_measurment(pk)
        return HttpResponse(deleted_measurment, 'application/json')
    
    
# Create your views here.
