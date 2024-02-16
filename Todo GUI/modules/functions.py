FILEPATH ="todos.txt"

def print_enum_array(list):
    """ Takes in array and prints each element with index offset by 1 """
    for index, item in enumerate(list):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)

def read_file(path):
    with open(path, 'r') as file:
        file_array = file.readlines()
    return file_array
    
def write_file(file_array, path):
    with open(path, 'w') as file:
        file.writelines(file_array)

def add_new_todo(todo_array, edit_index, date):
    todo = input("Enter a todo: ")
    todo = f"{todo} (Added: {date})\n"
    todo_array[edit_index] = todo 

def get_todo_index(action):
    index = int(input(f"Index of todo to {action}: "))
    index_offset = 1
    index = index - index_offset
    return index