import sqlite3

conn = sqlite3.connect('todo.sqlite')
cursor = conn.cursor()

query_todo_table = '''
SELECT *
FROM todo;
'''

cursor.execute(query_todo_table)

retrieved_todo = cursor.fetchall()

for todo in retrieved_todo:
    print(todo)

conn.close()
