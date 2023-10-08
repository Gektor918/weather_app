import json

from .models import WeatherInfo
from .serializers import WeatherInfoSerializer
import asyncio


def open_json():
    """
    Open json with city
    """
    with open('new_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


async def check_city(city_name):
    """
    Check in db entry city
    """
    queryset = WeatherInfo.objects.filter(city=city_name)
    return queryset


async def check_date_update(city_name):
    """
    Check in entry date_update 
    """
    queryset = WeatherInfo.objects.filter(city=city_name)
    date_update = [i.date_update async for i in queryset]
    return date_update


def create_or_update_entry(response_yandex_api, city_name):
    """
    Create or update a WeatherInfo record for the specified city using data from the Yandex Weather API.
    """
    data = response_yandex_api.json()
    temperature = data['fact']['temp']
    wind_speed = data['fact']['wind_speed']
    atmosphere_pressure = data['fact']['pressure_mm']

    try:
        weather_info = WeatherInfo.objects.get(city=city_name)
        
        weather_info.temperature = temperature
        weather_info.wind_speed = wind_speed
        weather_info.atmosphere_pressure = atmosphere_pressure
        weather_info.save()
        
        serializer = WeatherInfoSerializer(weather_info)
        print('Запись обновлена')

        return serializer
    except WeatherInfo.DoesNotExist:

        weather_info = WeatherInfo(
            city=city_name,
            temperature=temperature,
            wind_speed=wind_speed,
            atmosphere_pressure=atmosphere_pressure,
        )
        weather_info.save()

        print('Запись создана')
        serializer = WeatherInfoSerializer(weather_info)

        return serializer
