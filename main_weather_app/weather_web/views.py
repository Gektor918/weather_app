from datetime import timedelta

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .logic_service import *
from .serializers import WeatherInfoSerializer
from .yandex_api import *


class Weather(APIView):

    """
    This API view retrieves weather information for a specified city.
    
    It accepts a 'city' parameter in the request's query parameters and returns
    weather data for that city. If the data for the city is not in the database
    or is older than 30 minutes, it fetches the latest data from an external API.
    """
    
    def get(self, request):
        city_name = request.query_params.get('city').lower()
        
        if not city_name:
            return Response({'error': 'Параметр "city" не указан в запросе.'}, status=400)

        data = open_json()

        if not city_name in data: 
            return Response({'error': 'Такого города не существует.'}, status=400)
        else:
            queryset = asyncio.run(check_city(city_name))  
            
            if queryset.exists():
                date_update = asyncio.run(check_date_update(city_name))
    
                if timezone.localtime(timezone.now()) - date_update[0] > timedelta(minutes=30):
                    response_yandex_api = asyncio.run(request_api(city_name, data))
                    serializer = create_or_update_entry(response_yandex_api, city_name)
                    return Response(serializer.data, status=200)
                else:
                    serializer = WeatherInfoSerializer(queryset.first())
                    return Response(serializer.data, status=200)

            else:
                response_yandex_api = asyncio.run(request_api(city_name, data))

            if isinstance(response_yandex_api, requests.Response):
                if response_yandex_api.status_code == 200:
                    serializer = create_or_update_entry(response_yandex_api, city_name)
                    return Response(serializer.data, status=200)
            else:
                return Response({'error': 'Не удалось получить данные о погоде.'}, status=500)
