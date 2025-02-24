import sqlite3

def create_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        published_year INTEGER,
        is_read BOOLEAN
    )
    ''')

    conn.commit()
    conn.close()

def add_book(title, author, published_year, is_read):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO books (title, author, published_year, is_read)
    VALUES (?, ?, ?, ?)
    ''', (title, author, published_year, is_read))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def update_read_status(book_id, is_read):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE books
    SET is_read = ?
    WHERE id = ?
    ''', (is_read, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM books
    WHERE id = ?
    ''', (book_id,))
    conn.commit()
    conn.close()

def main():
    while True:
        print("\nДобро пожаловать в библиотеку!\n")
        print("1. Добавить книгу")
        print("2. Просмотреть все книги")
        print("3. Обновить статус прочтения")
        print("4. Удалить книгу")
        print("5. Выход")
        
        choice = input("Выберите операцию (1-5): ")
        
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            published_year = int(input("Введите год публикации: "))
            is_read = input("Книга прочитана? (yes/no): ") == 'yes'
            add_book(title, author, published_year, is_read)
            print("Книга добавлена!")
        
        elif choice == '2':
            books = view_books()
            print("\nСписок книг:")
            for book in books:
                print(f"{book[0]}. {book[1]} - {book[2]}, {book[3]} - Прочитана: {'Да' if book[4] else 'Нет'}")
        
        elif choice == '3':
            book_id = int(input("Введите ID книги для обновления статуса: "))
            is_read = input("Книга прочитана? (yes/no): ") == 'yes'
            update_read_status(book_id, is_read)
            print("Статус книги обновлен!")
        
        elif choice == '4':
            book_id = int(input("Введите ID книги для удаления: "))
            delete_book(book_id)
            print("Книга удалена!")
        
        elif choice == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")
   

if __name__ == '__main__':
    create_db()
    main()
