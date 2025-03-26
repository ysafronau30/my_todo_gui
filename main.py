import FreeSimpleGUI as sg
from functions import get_todos, write_todos

label = sg.Text('Enter todo')
add_button = sg.Button('Add', key='Add')
input_text = sg.InputText(key='todo')
edit_button = sg.Button('Edit', key='Edit')
list_box = sg.Listbox(get_todos(), size=(50,10), enable_events=True, key='todos')
layout = [[label, input_text, add_button], [list_box, edit_button], [complete_button, close_button]]

window = sg.Window("My To-do list", layout)

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = f"{values['todo'].capitalize().strip()}\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED | 'Cancel':
            break


