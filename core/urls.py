from django.urls import path
from .views import *
urlpatterns = [
     path('', Index.as_view(), name='index'),
     path('simulador/', simulador, name='simulador'),
     path('guiaFinceiro/', guiaFincanceiro, name='guiaFinceiro'),

]
