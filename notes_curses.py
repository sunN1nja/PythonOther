import curses
import sqlite3

def initialize_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY, title TEXT, content TEXT)''')
    conn.commit()
    conn.close()

def add_note(title, content):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT id, title, content FROM notes")
    notes = c.fetchall()
    conn.close()
    return notes

def update_note(note_id, new_title, new_content):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (new_title, new_content, note_id))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

def print_menu(stdscr, selected_idx, notes):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    menu = ["Создать заметку", "Редактировать заметку", "Удалить заметку", "Выйти"]

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_idx:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)

    # Печать заметок
    for idx, note in enumerate(notes):
        stdscr.addstr(0 + idx, 0, f"{note[0]}. [{note[1]}] {note[2]}")

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    selected_idx = 0

    while True:
        notes = get_notes()
        print_menu(stdscr, selected_idx, notes)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_idx > 0:
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < 3:
            selected_idx += 1
        elif key in [10, 13]:  # Enter key
            if selected_idx == 0:
                stdscr.clear()
                stdscr.addstr(0, 0, "Введите тему новой заметки (оставьте пустым, если нет): ")
                curses.echo()
                title = stdscr.getstr(1, 0, 60)  # Получаем байты
                if title:
                    title = title.decode('utf-8')  # Декодируем только если есть данные
                stdscr.addstr(2, 0, "Введите содержание новой заметки: ")
                content = stdscr.getstr(3, 0, curses.COLS - 1).decode('utf-8')
                add_note(title, content)
                curses.noecho()
            elif selected_idx == 1:
                stdscr.clear()
                stdscr.addstr(0, 0, "Введите ID заметки для редактирования: ")
                curses.echo()
                try:
                    note_id = int(stdscr.getstr(1, 0, 10).decode('utf-8'))
                    stdscr.addstr(2, 0, "Введите новую тему (оставьте пустым, если нет): ")
                    new_title = stdscr.getstr(3, 0, 60).decode('utf-8')
                    stdscr.addstr(4, 0, "Введите новое содержание: ")
                    new_content = stdscr.getstr(5, 0, curses.COLS - 1).decode('utf-8')
                    update_note(note_id, new_title, new_content)
                except (UnicodeDecodeError, ValueError):
                    stdscr.addstr(6, 0, "Ошибка ввода.")
                    stdscr.getch()
                curses.noecho()
            elif selected_idx == 2:
                stdscr.clear()
                stdscr.addstr(0, 0, "Введите ID заметки для удаления: ")
                curses.echo()
                try:
                    note_id = int(stdscr.getstr(1, 0, 10).decode('utf-8'))
                    delete_note(note_id)
                except (UnicodeDecodeError, ValueError):
                    stdscr.addstr(2, 0, "Ошибка ввода.")
                    stdscr.getch()
                curses.noecho()
            elif selected_idx == 3:
                break
        stdscr.refresh()

if __name__ == "__main__":
    initialize_db()
    curses.wrapper(main)
