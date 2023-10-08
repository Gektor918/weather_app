import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_weather_app.settings')

django.setup()

from weather_web.logic_service import open_json, check_city, check_date_update, create_or_update_entry
from weather_web.yandex_api import request_api
from weather_web.serializers import WeatherInfoSerializer