while True:
    userInput = input("Enter add, edit, show, complete, exit :")
    userInput = userInput.strip()
    match userInput:
        case "add":
            todo = input("Enter task to add:") +"\n"
            # Read existing tasks
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Add new task
            todos.append(todo)

            # Write everything back (overwrite file)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case "edit":
            number = input("Enter task number to edit (You can choose show to check the number of todo to edit it starts from 1):")
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            existingTodo = todos[int(number)-1]
            editedTodo = input(f"Enter updated task to edit {existingTodo} :")+"\n"
            editedTodo = editedTodo
            todos[int(number)-1] = editedTodo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            for index, task in enumerate(todos):
                row = f"{index}-{task.strip()}"
                print(row)
        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for index, task in enumerate(todos):
                row =f"{index}-{task.strip()}"
                print(row)
        case "complete":
            number = int(input("Please enter the task number which of your task is complete :"))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            removeTodoTask = todos[number]
            todos.pop(number)
            print(removeTodoTask, 'Removed from todos list')
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "exit":
            break
print("End of the program!")
