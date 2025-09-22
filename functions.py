FILEPATH = 'todos.txt'

def get_todos():
    todos_local = []
    with open(FILEPATH, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos):
    with open(FILEPATH, 'w') as file:
        file.writelines(todos)

