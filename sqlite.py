import sqlite3



# создание подключения к базе данных(или создание базы данных, если она не существует)
conn = sqlite3.connect('example.db')

# создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PROMARY KEY, name TEXT, age INTEGER)""")

# вставка данных
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))

# сохранение изменений
conn.commit()

# запрос данных 
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# закрытие подключения
conn.close()