#Todo list

def print_enum_array(list):
    """ Takes in array and prints each element with index offset by 1 """
    for index, item in enumerate(list):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)

def read_file():
    with open('todos.txt', 'r') as file:
        file_array = file.readlines()
    return file_array
    
def write_file(file_array):
    with open('todos.txt', 'w') as file:
        file.writelines(file_array)

def add_new_todo(todo_array):
    todo = input("Enter a todo: ")  + '\n'
    todo_array[edit_index] = todo

def get_todo_index(action):
    index = int(input(f"Index of todo to {action}: "))
    index_offset = 1
    index = index - index_offset
    return index



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
        todo_array = read_file()
        todo_array.append(todo)
        write_file(todo_array)

    elif user_input.startswith('show'):

        todo_array = read_file()

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
                    print_enum_array(todo_array)
            except:
                print_enum_array(todo_array)
        else:
            print_enum_array(todo_array)

    elif user_input.startswith('edit'):
        todo_array = read_file()

        try:
            # if contains more than 'edit
            if len(user_input) > 4:
                
                #take characters after 'edit' and type cast to int, if error in casting go to expect
                edit_index = int(user_input[4:]) - 1

                # if input index equal to or less than size of array
                if len(todo_array) >= edit_index:
                    add_new_todo(todo_array)
                    write_file(todo_array)

                else:
                    edit_index = get_todo_index('edit')
                    add_new_todo(todo_array)
                    write_file(todo_array)
            
            # if input just contains edit
            else:
                edit_index = get_todo_index('edit')
                add_new_todo(todo_array)
                write_file(todo_array)

        except:
            edit_index = get_todo_index('edit')
            add_new_todo(todo_array)
            write_file(todo_array)

    elif user_input.startswith('complete'):
        todo_array = read_file()

        try:
            # if contains more than 'complete'
            if len(user_input) > 8:
                
                #take characters after 'complete' and type cast to int, if error in casting go to expect
                complete_index = int(user_input[8:]) - 1

                # if input index equal to or less than size of array
                if len(todo_array) >= edit_index:
                    todo_array.pop(complete_index)
                    write_file(todo_array)

                else:
                    complete_index = get_todo_index('complete')
                    todo_array.pop(complete_index)
                    write_file(todo_array)
            
            # if input just contains complete
            else:
                complete_index = get_todo_index('complete')
                todo_array.pop(complete_index)
                write_file(todo_array)

        except:
            complete_index = get_todo_index('complete')
            todo_array.pop(complete_index)
            write_file(todo_array)

    elif user_input.startswith('exit'):
        break