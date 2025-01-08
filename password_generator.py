import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Базовые наборы символов
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Объединяем все выбранные символы
    all_characters = lowercase + uppercase + numbers + special_chars

    # Проверяем, есть ли доступные символы
    if not all_characters:
        raise ValueError("Убедитесь, что хотя бы один набор символов выбран.")

    # Генерируем пароль
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Генератор паролей")
    length = int(input("Введите желаемую длину пароля: "))
    use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    use_numbers = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_special_chars = input("Использовать специальные символы? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Сгенерированный пароль: {password}")

if __name__ == "__main__":
    main()
