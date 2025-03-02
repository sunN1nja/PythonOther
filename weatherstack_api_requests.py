import requests

# Ваш API ключ (полученный после регистрации)
api_key = 'your_api_key_here'

# Функция для получения погоды по названию города
def get_weather(city):
    # Формируем URL запроса
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем статус ответа
    if response.status_code == 200:
        data = response.json()  # Преобразуем ответ в формат JSON

        # Извлекаем необходимые данные
        city_name = data['location']['name']
        country = data['location']['country']
        temperature = data['current']['temperature']
        weather_description = data['current']['weather_descriptions'][0]

        # Выводим информацию о погоде
        print(f"Погода в городе {city_name}, {country}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {weather_description}")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

# Запрашиваем название города у пользователя
city = input("Введите название города: ")

# Получаем и отображаем погоду
get_weather(city)
