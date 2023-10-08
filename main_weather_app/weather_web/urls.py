from django.urls import path

from .views import *

urlpatterns = [
    path('weather', Weather.as_view(), name='weather'),
]
