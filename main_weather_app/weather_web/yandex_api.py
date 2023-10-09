import time

import aiohttp
import requests
from requests.exceptions import RequestException


async def request_api(city_name, data):

    api_key = 'd958356f-59a1-4617-8868-795a60a40f9c'
    headers = {'X-Yandex-API-Key': api_key}
    url = "https://api.weather.yandex.ru/v2/forecast/?lat={0}&lon={1}&lang=ru_RU".format(data[city_name]['lat'], data[(city_name)]['lot'])

    try:
        response = requests.get(url, headers=headers)
        time.sleep(3)
        return response
    except aiohttp.ClientError as e:
        print(f"Ошибка запроса: {e}")
