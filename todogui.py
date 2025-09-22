from time import strftime

import  FreeSimpleGUI as fsg
import  functions

fsg.theme('DarkPurple5')
clock = fsg.Text('', key='clock')
layout = fsg.Text("Type in a to do")
input_box = fsg.InputText(tooltip="Type in a to do", key="todoInput")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(), key="todoList", enable_events=True, size=(50, 10))
show_button = fsg.Button("Show")
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")
print(list_box)
window = fsg.Window("Todos",
                    [[layout],
                     [input_box,add_button],
                     [list_box, edit_button],
                     [complete_button,exit_button,clock]],
                    font=('Helvetica',15),resizable=True)
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=strftime("%H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            print(values['todoInput'])
            todos.append(values['todoInput']+"\n")
            functions.write_todos(todos)
            window['todoList'].update(values=todos)
        case 'Show':
            todos = functions.get_todos()
            for todo in todos:
                print(todo.strip())
        case 'Edit':
            try:
                todo_to_edit = values['todoList'][0]
                updated_to_do = values['todoInput']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = updated_to_do
                functions.write_todos(todos)
                window['todoList'].update(todos)
                window['todoInput'].update('')
            except IndexError:
                fsg.popup("Please select the task you want to edit")
        case "todoList":
            window['todoInput'].update(values['todoList'][0])
        case "Complete":
            try:
                todo_to_complete = values['todoList'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                window['todoList'].update(values=todos)
                functions.write_todos(todos)
            except IndexError:
                fsg.popup("Please select the task you want to Complete")
        case fsg.WINDOW_CLOSED :
            break
        case "Exit":
            break
window.close()