from django.shortcuts import render
from django.http import HttpRequest
from requests import get

from WeatherSite.settings import WEATHER_API_KEY


def index(request):
    return render(request, 'main_app/index.html')


def city(request: HttpRequest):
    # Параметры запроса
    params = {
        'q': request.GET.get(key='city', default='Москва'),
        'lang': 'ru',
        'units': 'metric',
        'appid': WEATHER_API_KEY,
    }

    # API запрос
    try:
        weather_data = get(
            'http://api.openweathermap.org/data/2.5/forecast?',
            params=params).json()['list'][0]
    except KeyError:
        err_context = {
            'error': 'Ошибка при получении данных'
        }
        return render(request, template_name='main_app/city.html', context=err_context)

    # Определение направления ветра
    deg = weather_data['wind']['deg']
    directions = ['С', 'СЗ', 'З', 'ЮЗ', 'Ю', 'ЮВ', 'В', 'СВ']
    direction = directions[int(((deg + 11.25) % 360) / 45)]

    # Контент
    context = {
        'city': (request.GET.get(key='city', default='Москва')).capitalize(),
        'weather_type': weather_data['weather'][0]['description'],
        'main': weather_data['main'],
        'wind_speed': weather_data['wind']['speed'],
        'wind_direction': direction
    }

    return render(request, template_name='main_app/city.html', context=context)
