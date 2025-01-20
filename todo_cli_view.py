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


def show_todo_list(todo_list):
    retrieved_todo = todo_list.get_all_tasks()

    for task_id, task, status in retrieved_todo:
        if status == 0:
            nice_status = 'Pending'
        else:
            nice_status = 'Done'
        print(f'{task_id} - {task} [ {nice_status} ]')


def add_todo(todo_list):
    new_task = input('Enter a task to add: ')
    return new_task


def change_todo_status(todo_list):
    show_todo_list(todo_list)
    todo_index = int(input('Changes status of which item? '))
    return todo_index


def delete_task(todo_list):
    show_todo_list(todo_list)
    todo_index = int(input('Delete which item? '))
    return todo_index

