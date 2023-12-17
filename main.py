from modules import functions

while True:
    user_input = input("Type add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith('add'):

        # if contains more than 'add'
        if len(user_input) > 3:

            #take all characters after 'add' 
            todo = user_input[4:] + '\n'
        else:
            todo = input("Enter a todo: ") + '\n'

        # store file data in array, append new input and write to file
        todo_array = functions.read_file()
        todo_array.append(todo)
        functions.write_file(todo_array)

    elif user_input.startswith('show'):

        todo_array = functions.read_file()

        # if contains more than 'show'
        if len(user_input) > 4:
            try:
                #take characters after 'show' and type cast to int, if error in casting go to expect
                index = int(user_input[4:]) - 1
                print(index)

                # if index is equal to or less than size of array
                if len(todo_array) >= index:
                    print(f'{index + 1}-{todo_array[index]}')
                else:
                    functions.print_enum_array(todo_array)
            except:
                functions.print_enum_array(todo_array)
        else:
            functions.print_enum_array(todo_array)

    elif user_input.startswith('edit'):
        todo_array = functions.read_file()

        try:
            # if contains more than 'edit
            if len(user_input) > 4:
                
                #take characters after 'edit' and type cast to int, if error in casting go to expect
                edit_index = int(user_input[4:]) - 1

                # if input index equal to or less than size of array
                if len(todo_array) >= edit_index:
                    functions.add_new_todo(todo_array, edit_index)
                    functions.write_file(todo_array)

                else:
                    edit_index = functions.get_todo_index('edit')
                    functions.add_new_todo(todo_array, edit_index)
                    functions.write_file(todo_array)
            
            # if input just contains edit
            else:
                edit_index = functions.get_todo_index('edit')
                functions.add_new_todo(todo_array, edit_index)
                functions.write_file(todo_array)

        except:
            edit_index = functions.get_todo_index('edit')
            functions.add_new_todo(todo_array, edit_index)
            functions.write_file(todo_array)

    elif user_input.startswith('complete'):
        todo_array = functions.read_file()

        try:
            # if contains more than 'complete'
            if len(user_input) > 8:
                
                #take characters after 'complete' and type cast to int, if error in casting go to expect
                complete_index = int(user_input[8:]) - 1

                # if input index equal to or less than size of array
                if len(todo_array) >= edit_index:
                    todo_array.pop(complete_index)
                    functions.write_file(todo_array)

                else:
                    complete_index = functions.get_todo_index('complete')
                    todo_array.pop(complete_index)
                    functions.write_file(todo_array)
            
            # if input just contains complete
            else:
                complete_index = functions.get_todo_index('complete')
                todo_array.pop(complete_index)
                functions.write_file(todo_array)

        except:
            complete_index = functions.get_todo_index('complete')
            todo_array.pop(complete_index)
            functions.write_file(todo_array)

    elif user_input.startswith('exit'):
        break