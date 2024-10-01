# Лабораторная работа 2. Использование API openweathermap.org

1. Создание файла ```own_key.py```, который содержит ключ, со следующим кодом:
```python
my_api_key = 'ключ'
```

1. Создание файла ```getweatherdata.py```, который содержит функцию get_weather_data, которая принимает два параметра: place и api_key, со следующим кодом:
```python
from own_key import my_api_key # Импортируем API ключ из файла owm_key.py
import requests


def get_weather_data(place, api_key=None):
    if api_key is None:
        api_key = my_api_key 

    if not place:
        return None

    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        name = data['name']
        coord = data['coord']
        country = data['sys']['country']
        feels_like = data['main']['feels_like']
        timezone_offset = data['timezone'] / 3600
        timezone = f"UTC+{timezone_offset}" if timezone_offset >= 0 else f"UTC{timezone_offset}"

        return {
            "name": name,
            "coord": coord,
            "country": country,
            "feels_like": feels_like,
            "timezone": timezone
        }
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return None

if __name__ == '__main__':
    cities = ['Chicago', 'Saint Petersburg', 'Dhaka']

    for city in cities:
        weather_data = get_weather_data(city)  # Передаем ключ API автоматически
        if weather_data:
            print(f"Данные для {city}: {weather_data}")
```

- Формируется URL для запроса к API OpenWeatherMap, где передаются название города, ключ API и единицы измерения
- Выполняется GET-запрос на указанный URL, и результат сохраняется в переменной response
- Извлекаются необходимые данные о погоде
- Форматируется строка с часовым поясом, указывая на UTC и смещение в часах
- Возвращается строка, содержащая информацию о городе, координатах, стране, температуре по ощущениям и часовом поясе


## Вывод
![image](https://github.com/user-attachments/assets/71a9f1b4-cce1-4e85-a7f3-05e2a8316a1e)
