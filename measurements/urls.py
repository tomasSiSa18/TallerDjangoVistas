from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.measurments_view, name='measurments_view'),
    path('<int:pk>', views.measurment_view, name='measurment_view'),
]