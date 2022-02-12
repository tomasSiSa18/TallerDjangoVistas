import measurements
from ..models import Measurement
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath('...'))
from variables.logic import variables_logic

def get_measurments():
    measurments = Measurement.objects.all()
    return measurments

def get_measurment(measurment_pk):
    measurment = Measurement.objects.get(pk=measurment_pk)
    return measurment

def update_measurment(measurment_pk, new_measurment):
    variable = variables_logic.get_variable(new_measurment["fields"]["variable"])

    measurment = get_measurment(measurment_pk)
    measurment.place = new_measurment["fields"]["place"]
    measurment.variable = variable
    measurment.value = float(new_measurment["fields"]["value"])
    measurment.unit = new_measurment["fields"]["unit"]
    measurment.dateTime = datetime.strptime(new_measurment["fields"]["dateTime"].replace("T", " ")[:18], '%Y-%m-%d %H:%M:%S')
    measurment.save()
    
    return measurment

def create_measurment(m):
    variable = variables_logic.get_variable(m["fields"]["variable"])
    measurement = Measurement(place=m["fields"]["place"], variable=variable, value=m["fields"]["value"], unit=m["fields"]["unit"], dateTime=m["fields"]["dateTime"])
    measurement.save()
    return measurement

def delete_measurment(measurment_pk):
    measurment = get_measurment(measurment_pk)
    measurment.delete()
    return measurment