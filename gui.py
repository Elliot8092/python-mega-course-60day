# Modules
import time
import PySimpleGUI as gui

# Local Module
from modules import functions

lable = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.read_file(), key="todo_entry",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")

window = gui.Window('My To-Do app', 
                    layout=[[lable, input_box, add_button],
                            [list_box, edit_button]], 
                    font=('Helvetica', 15))

# if one variable will store as a tuple
date = time.strftime('%d-%m-%y')

while True:
    event, value = window.read()
    print(event)
    print(value["todo"])
    print(value["todo_entry"][0])
    match event:
        case "Add":
            todo_array = functions.read_file()
            todo = f"{value['todo']} (Added: {date})\n"
            todo_array.append(todo)
            # list_box.Values = todo_array
            functions.write_file(todo_array)

        case "Edit":
            todo_to_edit = value["todo_entry"][0]
            new_todo = value['todo']
            todo_array = functions.read_file()
            index = todo_array.index(todo_to_edit)
            todo_array[index] = new_todo
            functions.write_file(todo_array)
            window['todo_entry'].update(values=todo_array)
        
        case "todo_entry":
            window['todo'].update(value = value["todo_entry"][0])

        case gui.WIN_CLOSED:
            break

window.close()


