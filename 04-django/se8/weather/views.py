import random
from django.shortcuts import render, redirect, get_object_or_404
import requests
from . import models
from .forms import CityForm

def add_city(request):
  if request.method == "POST":
    form = CityForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('all_city')      
  else:
    form = CityForm()

  return render(request, 'add_city.html', {'form': form})

def detail_city(request, id):
  city = get_object_or_404(models.City, id=id)
  
  lat, lon = city.lat, city.lon
  
  link = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}' 
  link += '&current_weather=true'

  try:
    dict1 = requests.get(link).json()
    temp = dict1["current_weather"]["temperature"]
  except:
    print(dict1)
    temp = "خطا"

  context = {
        'temp': temp,
        'city': city
      }
      
  return render(request, "detail_city.html", context)

def all_city(request):
  cities = models.City.objects.all()
  return render(request, 'cities.html', {'cities': cities})

def index(request):
  city = models.City.objects.all().first()
  if not city:
    return render(request, "error.html")
  
  lat, lon = city.lat, city.lon
  
  link = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}' 
  link += '&current_weather=true'

  try:
    dict1 = requests.get(link).json()
    temp = dict1["current_weather"]["temperature"]
  except:
    print(dict1)
    temp = "خطا"

  context = {
        'temp': temp,
        'city': city.title
      }
    
  return render(request, "index.html", context)

def index2(request):
  return redirect('/?lat=32.2&lon=32.35')
  context = {
      'temp': 'index2'
    }
  return render(request, "index.html", context)
