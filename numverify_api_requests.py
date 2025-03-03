import requests

# Ваш API ключ от numverify
api_key = 'API_KEY'

# Функция для проверки номера телефона
def check_phone_number(phone_number):
    # Формируем URL запроса
    url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}'

    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем статус ответа
    if response.status_code == 200:
        data = response.json()  # Преобразуем ответ в формат JSON
        
        # Проверяем, существует ли номер телефона в базе данных
        if data['valid']:
            country = data['country_name']
            location = data['location']
            carrier = data['carrier']
            line_type = data['line_type']

            # Выводим информацию о номере
            print(f"Номер {phone_number} является валидным!")
            print(f"Страна: {country}")
            print(f"Город: {location}")
            print(f"Оператор: {carrier}")
            print(f"Тип линии: {line_type}")
        else:
            print(f"Номер {phone_number} не является валидным.")
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

# Запрашиваем номер телефона у пользователя
phone_number = input("Введите номер телефона для проверки: ")

# Проверяем номер
check_phone_number(phone_number)
