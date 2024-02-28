FILEPATH ="todos.txt"

def read_file(path):
    with open(path, 'r') as file:
        file_array = file.readlines()
    return file_array
    
def write_file(file_array, path):
    with open(path, 'w') as file:
        file.writelines(file_array)