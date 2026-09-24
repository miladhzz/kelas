import requests
from django.shortcuts import render


def show_temp_view(request):
    city = request.GET.get("city")
    lat = request.GET["lat"]
    lon = request.GET["lon"]
    url= f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
    url += "&current_weather=true"
    
    try:
        data=requests.get(url).json()
        temp=data["current_weather"]["temperature"]
    except:
        temp=None

    context={'city':city,'temp':temp}
    return render(request,'show_temp.html',context)
