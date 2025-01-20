import sqlite3

class TodoModel:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def create_table_if_needed(self):
        create_todo_table = '''
        CREATE TABLE IF NOT EXISTS todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status BOOLEAN NOT NULL
        );'''

        self.cursor.execute(create_todo_table)

        self.conn.commit()

    def tidy_up(self):
        self.conn.close()

    def add_example_tasks(self):
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

        self.cursor.executemany(populate_todo_parametrized, todo_data)

        self.conn.commit()

    def get_all_tasks(self):
        query_todo_table = '''
            SELECT *
            FROM todo;
            '''

        self.cursor.execute(query_todo_table)

        return self.cursor.fetchall()

    def add_todo(self, new_task):
        populate_todo_parametrized = '''
        INSERT INTO
        todo (task, status)
        VALUES (?, ?);
        '''

        todo_data = (new_task, False)

        self.cursor.execute(populate_todo_parametrized, todo_data)

        self.conn.commit()

    def flip_todo_status(self, todo_index):
        get_status_of_item_parametrized = '''
        SELECT task, status
        FROM todo
        WHERE id=?;
        '''

        self.cursor.execute(get_status_of_item_parametrized, (todo_index,))
        task, status = self.cursor.fetchone()

        mark_todo_done_parametrized = '''
        UPDATE todo
        SET status=?
        WHERE id=?;
        '''

        todo_data = not status, todo_index

        self.cursor.execute(mark_todo_done_parametrized, todo_data)

        self.conn.commit()

    def delete_todo(self, todo_index):
        delete_todo_parametrized = '''
            DELETE FROM todo
            WHERE id = ?;
            '''

        todo_data = todo_index,

        self.cursor.execute(delete_todo_parametrized, todo_data)

        self.conn.commit()

    def format_task(self, task_id, task, status):
        return f'{task_id} - {task} [ status: {status} ]'

