import sqlite3

conn = sqlite3.connect('todo.sqlite')
cursor = conn.cursor()

create_todo_table = '''
CREATE TABLE IF NOT EXISTS todo 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT NOT NULL,
status BOOLEAN NOT NULL
);'''

cursor.execute(create_todo_table)

conn.close()
