import todo_model as tdm
import todo_cli_view as tdv

FILENAME = 'todo.sqlite'

todo_list = tdm.TodoModel(FILENAME)

todo_list.create_table_if_needed()
todo_list.add_example_tasks()

managing = True

while managing:
    tdv.show_todo_list(todo_list)

    choice = tdv.get_choice()

    match choice:
        case '1':
            new_task = tdv.add_todo(todo_list)
            todo_list.add_todo(new_task)

        case '2':
            todo_index = tdv.change_todo_status(todo_list)
            todo_list.flip_todo_status(todo_index)

        case '3':
            todo_index = tdv.delete_task(todo_list)
            todo_list.delete_todo(todo_index)

        case '4':
            managing = False


