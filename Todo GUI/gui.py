# Modules
import time
import PySimpleGUI as gui
import os

# Local Module
from modules import functions

# if file does not exist, create
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

if not os.path.exists("todos.txt"):
    with open("completed.txt", "w") as file:
        pass

lable = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
todo_box = gui.Listbox(values=functions.read_file("todos.txt"), key="todo_entry",
                       enable_events=True, size=[45, 10])
completed_box = gui.Listbox(values=functions.read_file("completed.txt"), key="complete_entry",
                       enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit", visible=False)
complete_button = gui.Button("Complete", visible=False)
delete_button = gui.Button("Delete", visible=False)
exit_button = gui.Button("Exit")

window = gui.Window('My To-Do app', 
                    layout=[[lable, input_box, add_button],
                            [todo_box, completed_box],
                            [edit_button, complete_button, delete_button],
                            [exit_button]], 
                    font=('Helvetica', 15))

# if one variable will store as a tuple
date = time.strftime('%d-%m-%y')

while True:
    # event = selected action, value = input box value
    event, value = window.read()
    match event:
        case "Add":
            if value['todo'] != "":

                todo_array = functions.read_file("todos.txt")
                todo = value['todo'] + "\n"
                todo_array.append(todo)
                functions.write_file(todo_array, "todos.txt")

                # refresh window with updated array values
                window['todo_entry'].update(values=todo_array)

                # clear input box
                window['todo'].update(value="")

        case "Edit":
            list_length = len(value["todo_entry"])

            # check that todo has been selected before pressing edit
            if list_length >= 1:
                todo_to_edit = value["todo_entry"][0]
            
                # Take todo value from input_box
                new_todo = value['todo']
                
                todo_array = functions.read_file("todos.txt")
                
                # get index for selected todo
                index = todo_array.index(todo_to_edit)
                
                # replace selected todo
                todo_array[index] = new_todo + "\n"

                functions.write_file(todo_array, "todos.txt")

                # refresh window with updated array values
                window['todo_entry'].update(values=todo_array)

                # Remove buttons
                window['Edit'].update(visible=False)
                window['Complete'].update(visible=False)
                window['Delete'].update(visible=False)

                # clear input box
                window['todo'].update(value="")

        case "Complete":
            list_length = len(value["todo_entry"])
        
            # check that todo has been selected before pressing complete
            if list_length >= 1:

                # get selected value from todo_list
                todo_to_complete = value["todo_entry"][0]

                # Read files
                todo_array = functions.read_file("todos.txt")
                complete_array = functions.read_file("completed.txt")

                # get index for selected todo
                index = todo_array.index(todo_to_complete)
                complete_array.append(todo_array[index])
                todo_array.pop(index)

                # Write files
                functions.write_file(todo_array, "todos.txt")
                functions.write_file(complete_array, "completed.txt")
                
                # refresh window with updated array values
                window['todo_entry'].update(values=todo_array)
                window['complete_entry'].update(values=complete_array)
                # clear input box
                window['todo'].update(value="")

                # Remove buttons
                window['Edit'].update(visible=False)
                window['Complete'].update(visible=False)
                window['Delete'].update(visible=False)


        case "Delete":
            list_length = len(value["todo_entry"])
        
            # check that todo has been selected before pressing updating
            if list_length >= 1:
    
                todo_to_delete = value["todo_entry"][0]

                todo_array = functions.read_file("todos.txt")
                
                # get index for selected todo
                index = todo_array.index(todo_to_delete)

                todo_array.pop(index)

                functions.write_file(todo_array, "todos.txt")

                # refresh window with updated array values
                window['todo_entry'].update(values=todo_array)
                # clear input box
                window['todo'].update(value="")

               # Remove buttons
                window['Edit'].update(visible=False)
                window['Complete'].update(visible=False)
                window['Delete'].update(visible=False)

        # Update todo to selected
        case "todo_entry":
            list_length = len(value["todo_entry"])

            # check that todo has been selected before pressing updating
            if list_length >= 1:
                # Remove trailing new line
                selected_todo = value["todo_entry"][0]
                selected_todo = selected_todo.rstrip()
                
                window['todo'].update(value = selected_todo)

                # Show buttons
                window['Edit'].update(visible=True)
                window['Complete'].update(visible=True)
                window['Delete'].update(visible=True)


        case "Exit":
            break

        case gui.WIN_CLOSED:
            break

window.close()


