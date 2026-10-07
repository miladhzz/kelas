import random
from django.shortcuts import render, redirect
import requests

def index(request):
  lat = request.GET.get('lat')
  lon = request.GET.get('lon')
  if lon is None or lat is None:
     return render(request, "error.html")
  
  link = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}' 
  link += '&current_weather=true'

  try:
    dict1 = requests.get(link).json()
    temp = dict1["current_weather"]["temperature"]
  except:
    print(dict1)
    temp = "خطا"

  context = {
        'temp': temp
      }
    
  return render(request, "index.html", context)

def index2(request):
  return redirect('/?lat=32.2&lon=32.35')
  context = {
      'temp': 'index2'
    }
  return render(request, "index.html", context)
