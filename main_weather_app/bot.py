import logging
from datetime import timedelta

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from django.utils import timezone

from weather_bot.django_bot import *

bot = Bot(token='6493629924:AAF5r1MIvyjRQo46gYTst4jMmgtWiweWj0A')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Узнать погоду")
    keyboard.add(button)

    await message.answer("Привет! Я бот. Нажми кнопку:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Узнать погоду")
async def process_button_click(message: types.Message):
    await message.reply("Введите город:")


data = open_json()
@dp.message_handler(lambda message: (message.text).lower() not in data)
async def process_button_click(message: types.Message):
    await message.reply("Нет такого города в том списке, который я использую ( , попробуйте еще раз!")


@dp.message_handler(lambda message:  (message.text).lower() in data)
async def process_button_click(message: types.Message):

    city_name = (message.text).lower()
    queryset = await check_city(city_name)

    if queryset.exists:
        date_update = await check_date_update(city_name)

        if date_update != []:

            if timezone.localtime(timezone.now()) - date_update[0] > timedelta(minutes=30):
                await message.reply("Подождите несколько секунд...")
                
                response_yandex_api = await request_api(city_name, data)
                data_info = open_json()
                data_info = response_yandex_api.json()

                temperature = data_info['fact']['temp']
                wind_speed = data_info['fact']['wind_speed']
                atmosphere_pressure = data_info['fact']['pressure_mm']
                final_string = ""
                final_string += f"Город: {city_name},\nТемпература: {temperature},\nСкорость ветра: {wind_speed},\nДавление: {atmosphere_pressure}\n"

                await message.reply(final_string)
            else:
                result_string = ""
                async for weather_info in queryset:
                    result_string += f"Город: {weather_info.city},\n Температура: {weather_info.temperature},\n Скорость ветра: {weather_info.wind_speed},\n Давление: {weather_info.atmosphere_pressure}\n"
                await message.reply(result_string)
        else:
            await message.reply("Подождите несколько секунд делаем запрос...")
                
            response_yandex_api = await request_api(city_name, data)
            data_info = open_json()
            data_info = response_yandex_api.json()

            temperature = data_info['fact']['temp']
            wind_speed = data_info['fact']['wind_speed']
            atmosphere_pressure = data_info['fact']['pressure_mm']
            final_string = ""
            final_string += f"Город: {city_name},\nТемпература: {temperature},\nСкорость ветра: {wind_speed},\nДавление: {atmosphere_pressure}\n"

            await message.reply(final_string)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
