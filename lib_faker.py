from faker import Faker

def show_faker_examples():
    fake = Faker()

    print("=== Примеры использования библиотеки Faker ===")
    
    # Генерация личной информации
    print("\n1. Личная информация:")
    print("Имя:", fake.first_name())
    print("Фамилия:", fake.last_name())
    print("Полное имя:", fake.name())
    print("Email:", fake.email())
    print("Телефон:", fake.phone_number())
    
    # Генерация адреса
    print("\n2. Адрес:")
    print("Улица:", fake.street_address())
    print("Город:", fake.city())
    print("Штат:", fake.state())
    print("ZIP-код:", fake.zipcode())
    print("Полный адрес:", fake.address())
    
    # Генерация компании
    print("\n3. Информация о компании:")
    print("Название компании:", fake.company())
    print("Должность:", fake.job())
    
    # Генерация даты
    print("\n4. Даты:")
    print("Дата рождения:", fake.date_of_birth())
    print("Будущая дата:", fake.future_date())
    print("Прошлая дата:", fake.past_date())
    
    # Генерация текста
    print("\n5. Текст:")
    print("Случайный текст:", fake.text())
    print("Случайное предложение:", fake.sentence())
    
    # Генерация интернет-данных
    print("\n6. Интернет-данные:")
    print("URL:", fake.url())
    print("IP-адрес:", fake.ipv4())
    print("Случайный домен:", fake.domain_name())
    
    # Генерация кредитной карты
    print("\n7. Кредитные карты:")
    print("Номер кредитной карты:", fake.credit_card_number())
    print("Тип кредитной карты:", fake.credit_card_provider())
    
    # Генерация различных данных
    print("\n8. Разные данные:")
    print("Случайное число:", fake.random_number())
    print("Случайная строка:", fake.word())
    print("Случайный цвет:", fake.color_name())

if __name__ == "__main__":
    show_faker_examples()
