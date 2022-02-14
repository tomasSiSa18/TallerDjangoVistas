from ..models import Measurement
import variables.logic.variables_logic as variables

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(me_pk):
    measurement = Measurement.objects.get(pk=me_pk)
    return measurement

def update_measurement(me_pk, new_me):
    measurement = get_measurement(me_pk)
    measurement.value = new_me["value"]
    measurement.save()
    return measurement

def create_measurement(me):
    var = variables.get_variable(me["variable"])
    measurement = Measurement(variable=var, value=me["value"], unit=me["unit"],place=me["place"])
    measurement.save()
    return measurement

def delete_measurement(me_pk):
    measurement = get_measurement(me_pk)
    measurement.delete()
    return measurement