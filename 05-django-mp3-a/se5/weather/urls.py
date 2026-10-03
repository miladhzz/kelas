from django.urls import path
from .views import show_temp_view, show_all_city, add_city


urlpatterns = [
    path('', show_temp_view, name='home'),
    path('all-city/', show_all_city, name='show_all_city'),
    path('add-city/', add_city, name='add_city'),
]
