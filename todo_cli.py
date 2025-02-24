# Нужна папка data рядом со скриптом
import sqlite3

def connect_to_db():
    return sqlite3.connect('data/todo.db')

def create_table():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
    )
    ''')

    connection.commit()
    connection.close()

def add_task(title):
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, 0))
    
    connection.commit()
    connection.close()

def get_tasks():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    connection.close()
    return tasks

def update_task(task_id, completed):
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))

    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))

    connection.commit()
    connection.close()

def menu():
    while True:
        print("\nToDo приложение")
        print("1. Добавить задачу")
        print("2. Посмотреть задачи")
        print("3. Обновить задачу")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название задачи: ")
            add_task(title)
            print("Задача добавлена!")

        elif choice == '2':
            tasks = get_tasks()
            if tasks:
                print("\nСписок задач:")
                for task in tasks:
                    status = "✓" if task[2] else "✗"
                    print(f"{task[0]}. {task[1]} [{status}]")
            else:
                print("Нет задач!")

        elif choice == '3':
            task_id = int(input("Введите ID задачи для обновления: "))
            completed = input("Статус выполнения (y/n): ").lower() == 'y'
            update_task(task_id, 1 if completed else 0)
            print("Задача обновлена!")

        elif choice == '4':
            task_id = int(input("Введите ID задачи для удаления: "))
            delete_task(task_id)
            print("Задача удалена!")

        elif choice == '5':
            print("Выход из приложения...")
            break

        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == '__main__':
    create_table()
    menu()
