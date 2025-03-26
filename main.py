import FreeSimpleGUI as sg
import functions
import time

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
add_button = sg.Button('Add')
input_text = sg.InputText(key='todo')
edit_button = sg.Button('Edit')
list_box = sg.Listbox(functions.get_todos(), size=[45,10], enable_events=True, key='todos')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
sg.theme('Black')
layout = [[clock],[label, input_text, add_button], [list_box, edit_button, complete_button], [exit_button]]

window = sg.Window("My To-do list", layout, font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=100)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = f"{values['todo'].capitalize().strip()}\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select the item first', font=('Helvetica', 15))
        case 'todos':
            window['todo'].update(value=values['todos'][0][:-1])
        case 'Complete':
            try:
                todos = functions.get_todos()
                completed_todo = values['todos'][0]
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select the item first', font=('Helvetica', 15))
        case sg.WIN_CLOSED | 'Exit' | 'Cancel':
            break
    window['clock'].update(value=time.strftime('%B %d, %Y %H:%M:%S'))

window.close()