from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all-city/', views.all_city, name="all_city"),
    path('index2/', views.index2, name="index2"),
]
