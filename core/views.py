from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.generic import View
from django.http import JsonResponse
class Index(View):
     def get(self, request):
          return render(request, 'index.html')

class Cotacao(View):
     def get(self, request):
          return render(request, 'cotacao.html')
# views.py

def simulador(request):
    return render(request, 'simulador.html')
def guiaFincanceiro(request):
    return render(request, 'guiaFincanceiro.html')
