from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse("index 1")

def index2(request):
  return HttpResponse("index 2")

def index3(request):
  return HttpResponse("index 3")

def index4(request):
  return HttpResponse("index 4")

def index5(request):
  return HttpResponse("index 5")
