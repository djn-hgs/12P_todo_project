import sqlite3

def show_todo_list(cursor):
    query_todo_table = '''
    SELECT *
    FROM todo;
    '''

    cursor.execute(query_todo_table)

    retrieved_todo = cursor.fetchall()

    for task_id, task, status in retrieved_todo:
        if status == 0:
            nice_status = 'Pending'
        else:
            nice_status = 'Done'
        print(f'{task_id} - {task} [ {nice_status} ]')




def get_choice():
    choices = {
        '1': 'Add todo',
        '2': 'Flip todo status',
        '3': 'Delete todo',
        '4': 'Quit'
    }

    print('Make a choice:')

    for i, c in choices.items():
        print(f'{i} - {c}')

    choice_made = None

    while not choice_made:
        my_choice = input('Enter your choice: ')

        if my_choice in choices:
            choice_made = my_choice

    return choice_made

def add_todo(cursor):
    new_task = input('Enter a task to add: ')

    populate_todo_parametrized = '''
    INSERT INTO
    todo (task, status)
    VALUES (?, ?);
    '''

    todo_data = (new_task, False)

    cursor.execute(populate_todo_parametrized, todo_data)


def mark_todo_done(cursor):
    todo_index = int(input('Changes status of which item? '))

    get_status_of_item_parametrized = '''
    SELECT task, status
    FROM todo
    WHERE id=?;
    '''

    cursor.execute(get_status_of_item_parametrized, (todo_index,))
    (task, status) = cursor.fetchone()

    mark_todo_done_parametrized = '''
    UPDATE todo
    SET status=?
    WHERE id=?;
    '''

    todo_data = (not status, todo_index)

    cursor.execute(mark_todo_done_parametrized, todo_data)


def delete_todo(cursor):
    todo_index = int(input('Delete which item? '))

    delete_todo_parametrized = '''
        DELETE FROM todo
        WHERE id = ?;
        '''

    todo_data = todo_index,

    cursor.execute(delete_todo_parametrized, todo_data)

todo_conn = sqlite3.connect('todo.sqlite')
todo_cursor = todo_conn.cursor()

managing = True

while managing:
    show_todo_list(todo_cursor)

    choice = get_choice()


    match choice:
        case '1':
            add_todo(todo_cursor)
        case '2':
            mark_todo_done(todo_cursor)
        case '3':
            delete_todo(todo_cursor)
        case '4':
            managing = False

    todo_conn.commit()

todo_conn.close()
