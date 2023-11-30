from django.urls import path
from .views import *
urlpatterns = [
     path('', Index.as_view(), name='index'),
     path('simulador/', simulador, name='simulador'),
     path('guiaFinceiro/', guiaFincanceiro, name='guiaFinceiro'),
     path('novoInvestidor/', novo_investidor, name='novo_investidor'),
]
