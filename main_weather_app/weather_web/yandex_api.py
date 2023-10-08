import requests
from requests.exceptions import RequestException
import time


# def request_api(city_name, data):
#     """
#     Send a request to the Yandex Weather API to fetch weather data for the specified city.
#     """
#     api_key = 'd958356f-59a1-4617-8868-795a60a40f9c'
#     headers = {'X-Yandex-API-Key': api_key,}
#     url = "https://api.weather.yandex.ru/v2/forecast/?lat={0}&lon={1}&lang=ru_RU".format(data[city_name]['lat'], data[city_name]['lot'])

#     try:
#         response = requests.get(url, headers=headers)
#         return response
#     except RequestException as e:
#         print (f"Ошибка запроса: {e}")



import aiohttp

async def request_api(city_name, data):
    """
    Send an asynchronous request to the Yandex Weather API to fetch weather data for the specified city.
    """
    api_key = 'd958356f-59a1-4617-8868-795a60a40f9c'
    headers = {'X-Yandex-API-Key': api_key}
    url = "https://api.weather.yandex.ru/v2/forecast/?lat={0}&lon={1}&lang=ru_RU".format(data[city_name]['lat'], data[(city_name)]['lot'])

    #async with aiohttp.ClientSession() as session:
    try:
        response = requests.get(url, headers=headers)
        time.sleep(3)
        return response
    except aiohttp.ClientError as e:
        print(f"Ошибка запроса: {e}")




    # async with aiohttp.ClientSession() as session:
    #     try:
    #         async with session.get(url, headers=headers) as response:
    #             #response.raise_for_status()  # Проверяем на наличие ошибок в ответе
    #             time.sleep(3)
    #             return response
    #     except aiohttp.ClientError as e:
    #         print(f"Ошибка запроса: {e}")