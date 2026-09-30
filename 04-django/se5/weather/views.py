import random
from django.shortcuts import render
import requests

def index(request):
  link = 'https://api.open-meteo.com/v1/forecast?latitude=34.7981&longitude=48.5146' 
  link += '&current_weather=true'

  try:
    dict1 = requests.get(link).json()
    temp = dict1["current_weather"]["temperature"]
  except:
    temp = "خطا"

  context = {
        'temp': temp
      }
    
  return render(request, "index.html", context)

def index2(request):
  context = {
      'temp': 'index2'
    }
  return render(request, "index.html", context)
