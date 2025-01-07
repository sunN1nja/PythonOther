def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль!"
    return x / y

def calculator():
    print("Добро пожаловать в CLI Калькулятор!")
    print("Введите 'exit' для выхода")

    while True:
        # Запрашиваем ввод пользователя
        user_input = input("\nВведите выражение (например, 2 + 2) или 'exit': ")

        if user_input.lower() == 'exit':
            print("Выход из программы. До свидания!")
            break

        try:
            # Разделяем ввод пользователя на части
            parts = user_input.split()
            if len(parts) != 3:
                print("Ошибка: введите выражение в формате 'число оператор число'")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Ошибка: Неподдерживаемый оператор. Используйте +, -, *, /")
                continue

            print(f"Результат: {result}")
        
        except ValueError:
            print("Ошибка: Введите корректные числа для вычисления.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    calculator()
