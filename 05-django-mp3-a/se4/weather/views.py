import requests
from django.shortcuts import render
from . import models

def show_all_city(request):
    cities = models.City.objects.all()
    return render(request, 'show_all_city.html', {'cities': cities})


def show_temp_view(request):
    id = request.GET.get("id")

    if id is None:
        return render(request,'error.html')

    city = models.City.objects.filter(id=id).first()
    lat, lon = city.lat, city.lon

    url= f"https://api.open-meteo.com/v1/forecast?"
    url += f"latitude={lat}&longitude={lon}"
    url += "&current_weather=true"
    
    try:
        data=requests.get(url).json()
        temp=data["current_weather"]["temperature"]
    except:
        return render(request,'error.html')

    context={'city':city,'temp':temp}
    return render(request,'show_temp.html',context)
