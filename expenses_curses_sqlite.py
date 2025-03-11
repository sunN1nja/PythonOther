import curses
import sqlite3

def main(stdscr):
    curses.curs_set(0)
    
    menu = ['Добавить расход', 'Просмотр расходов', 'Выход']
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        for idx, row in enumerate(menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu) // 2 + idx
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, row)
        
        stdscr.refresh()
        
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(menu) - 1:
                break
            if current_row == 0:
                add_expense(stdscr)
            elif current_row == 1:
                view_expenses(stdscr)

def add_expense(stdscr):
    curses.curs_set(1)
    stdscr.clear()

    curses.echo()
    
    try:
        stdscr.addstr(0, 0, "Введите дату (YYYY-MM-DD): ")
        stdscr.refresh()
        date = stdscr.getstr(1, 0, 20).decode('utf-8')

        stdscr.addstr(2, 0, "Введите категорию: ")
        stdscr.refresh()
        category = stdscr.getstr(3, 0, 20).decode('utf-8')

        stdscr.addstr(4, 0, "Введите сумму: ")
        stdscr.refresh()
        amount = stdscr.getstr(5, 0, 20).decode('utf-8')

        stdscr.addstr(6, 0, "Введите описание: ")
        stdscr.refresh()
        description = stdscr.getstr(7, 0, 50).decode('utf-8')

        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
            (date, category, float(amount), description)
        )
        conn.commit()
        conn.close()
        
        stdscr.addstr(9, 0, "Запись успешно добавлена. Нажмите любую клавишу, чтобы вернуться в меню.")

    except ValueError:
        stdscr.addstr(9, 0, "Ошибка ввода. Убедитесь в правильности данных и попробуйте снова.")
    except sqlite3.Error as e:
        stdscr.addstr(9, 0, f"Ошибка базы данных: {e}")
    except Exception as e:
        stdscr.addstr(9, 0, f"Произошла ошибка: {e}")

    curses.noecho()
    stdscr.getch()

def view_expenses(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    
    stdscr.addstr(0, 0, "{:<5} {:<12} {:<12} {:<8} {:<30}".format("ID", "Дата", "Категория", "Сумма", "Описание"))

    for idx, expense in enumerate(expenses):
        y = idx + 1
        ex_id, date, category, amount, description = expense
        stdscr.addstr(
            y, 0,
            "{:<5} {:<12} {:<12} {:<8.2f} {:<30}".format(ex_id, date, category, amount, description)
        )
    
    stdscr.addstr(len(expenses) + 2, 0, "Нажмите любую клавишу, чтобы вернуться в меню.")
    stdscr.getch()

def initialize_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

initialize_db()
curses.wrapper(main)
