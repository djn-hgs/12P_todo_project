import tkinter as tk


class ToDoApp(tk.Frame):
    def __init__(self, parent, todo_list):
        super().__init__(parent)

        self.todo_list = todo_list

        self.title = tk.Label(self, text="todo app")
        self.todo_display = ToDoDisplay(self, todo_list)
        self.add_button = tk.Button(self, text="Add", command=self.todo_display.add_item)
        self.del_button = tk.Button(self, text="Delete", command=self.todo_display.delete_item)

        self.title.grid(row=0,column=0,columnspan=2)
        self.todo_display.grid(row=1,column=0, columnspan=2)
        self.add_button.grid(row=2,column=0)
        self.del_button.grid(row=2, column=1)

class ToDoDisplay(tk.Frame):
    def __init__(self, parent, todo_list):
        super().__init__(parent)
        self.add_item_dialog = None
        self.dialog_dict = None
        self.parent = parent
        self.task_widgets = {}
        self.todo_list = todo_list
        self.selected = tk.IntVar()
        self.response_var = tk.StringVar(self)
        self.check_box_state = tk.BooleanVar(self)
        self.update_view()

    def create_todo_widget(self, todo, index):
        task_radio = tk.Radiobutton(self, variable=self.selected, value=index)
        task_label = tk.Label(self, text=todo['task'])
        task_checkbox = tk.Checkbutton(self, variable=self.check_box_state, command=self.update_checkbox)

        task_radio.grid(row=index, column=0)
        task_label.grid(row=index, column=1)
        task_checkbox.grid(row=index, column=2)

        return [task_radio, task_label, task_checkbox]

    def update_view(self):
        for i, t in enumerate(self.todo_list):
            self.task_widgets[i] = self.create_todo_widget(t, i)

    def delete_item(self):
        task_to_delete = self.selected.get()

        print(task_to_delete)

        row_to_remove = self.task_widgets.pop(task_to_delete)

        for w in row_to_remove:
            w.destroy()

        self.todo_list.pop(task_to_delete)

        print(self.todo_list)



    def add_item(self):
        self.dialog_dict = {
            'message': 'Enter your task',
            'response': self.response_var,
            'callback': self.process_new_item
        }

        self.add_item_dialog = Dialog(self.parent, self.dialog_dict)
        self.add_item_dialog.grab_set()

    def update_checkbox(self):
        pass

    def process_new_item(self, event=None):
        response = self.response_var.get()

        new_task = {'task': response, 'status': False}

        self.todo_list.append(new_task)

        n = len(self.todo_list)

        new_widget = self.create_todo_widget(new_task, n)

        self.task_widgets[n] = new_widget

        self.add_item_dialog.close()
        self.response_var.set('')

        print(self.todo_list)


class Dialog(tk.Toplevel):
    def __init__(self, parent, dialog_dict):
        super().__init__(parent)
        self.label = tk.Label(self, text=dialog_dict['message'])
        self.entry = tk.Entry(self, textvariable=dialog_dict['response'])
        self.ok = tk.Button(self, text="Ok", command=dialog_dict['callback'])

        self.label.grid(row=0, column=0)
        self.entry.grid(row=1, column=0)
        self.ok.grid(row=2, column=0)

        self.entry.focus_set()
        self.bind('<Return>', dialog_dict['callback'])

    def close(self):
        self.label.destroy()
        self.entry.destroy()
        self.ok.destroy()
        self.destroy()


root = tk.Tk()

my_list = [
    {'task': 'Think of something to do', 'status': False},
    {'task': 'Add due dates', 'status': False}

]

my_app = ToDoApp(root, my_list)

my_app.pack()

root.mainloop()
