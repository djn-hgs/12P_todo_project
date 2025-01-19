import sqlite3

conn = sqlite3.connect('todo.sqlite')
cursor = conn.cursor()

create_todo_table = '''
CREATE TABLE IF NOT EXISTS todo (
id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT NOT NULL,
status BOOLEAN NOT NULL
);'''

cursor.execute(create_todo_table)

conn.commit()

populate_todo_parametrized = '''
INSERT INTO
todo (task, status)
VALUES (?, ?);
'''

todo_data = [
    ('Write todo list GUI', True),
    ('Create todo Database', True),
    ('Populate todo Database', False)
]

cursor.executemany(populate_todo_parametrized, todo_data)

conn.commit()

conn.close()
