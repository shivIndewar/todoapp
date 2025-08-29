todos=[]
while True:
    userInput = input("Enter add, edit, show, complete, exit :")
    userInput = userInput.strip()
    match userInput:
        case "add":
            todo = input("Enter task to add:")
            todos.append(todo)
        case "edit":
            number = input("Enter task number to edit (You can choose show to check the number of todo to edit it starts from 1):")
            existingTodo = todos[int(number)-1]
            editedTodo = input(f"Enter updated task to edit {existingTodo} :")
            editedTodo = editedTodo.strip()
            todos[int(number)-1] = editedTodo
        case "show":
            for index, task in enumerate(todos):
                row =f"{index}-{task}"
                print(row)
        case "complete":
            number = int(input("Please enter the task number which of your task is complete :"))
            removeTodoTask = todos[number]
            todos.pop(number)
            print(removeTodoTask, 'Removed from todos list')
        case "exit":
            break
print("End of the program!")
