import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from .forms import CityForm


@login_required
def add_city(request):       
    if request.method == "GET":
        form = CityForm()
        return render(request, 'add_city.html', {'form': form})
    else: 
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_all_city')
        else:
            return redirect('/')


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
