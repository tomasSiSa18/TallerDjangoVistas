
from ..models import Measurement
def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements
def create_measurement(var):
    measurement = Measurement(variable=var["variable"],value=var["value"],unit=var["unit"],place=var["place"],dateTime=var["dateTime"])
    measurement.save()
    
def update_measurement(var_pk,new_plc):
    measurement = get_measurement(var_pk)
    measurement.value =new_plc["value"]
    measurement.unit =new_plc["unit"]
    measurement.place =new_plc["place"]
    measurement.save()
    return measurement

def delete_measurements(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()
    return measurement
