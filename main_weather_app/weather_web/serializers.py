from .models import WeatherInfo
from rest_framework import serializers


class WeatherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = ['city', 'temperature', 'wind_speed', 'atmosphere_pressure']
