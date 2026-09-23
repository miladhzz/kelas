# from django.http import HttpResponse
from django.shortcuts import render

def show_temp_view(request):
  username = request.user.username
  return render(request, 'home.html', {'username': username})


# def show_temp_view(request):
#   if request.user.is_authenticated:
#     return HttpResponse("<h1>salam " + request.user.username + "</h1>")
#   else:
#     return HttpResponse("salam Guest")
