import  functions
while True:
    userInput = input("Enter add, edit, show, complete, exit :")
    userInput = userInput.strip()
    match userInput:
        case "add":
            todo = input("Enter task to add:")
            # Read existing tasks
            todos = functions.get_todos()
            # Add new task
            todos.append(todo+"\n")
            # Write everything back (overwrite file)
            functions.write_todos(todos)

        case "edit":
            number = input("Enter task number to edit (You can choose show to check the number of todo to edit it starts from 1):")
            todos = functions.get_todos()
            existingTodo = todos[int(number)-1]
            editedTodo = input(f"Enter updated task to edit {existingTodo} :")+"\n"
            editedTodo = editedTodo
            todos[int(number)-1] = editedTodo
            functions.write_todos(todos)

            for index, task in enumerate(todos):
                row = f"{index}-{task.strip()}"
                print(row)

        case "show":
            todos = functions.get_todos()
            for index, task in enumerate(todos):
                row =f"{index}-{task.strip()}"
                print(row)
        case "complete":
            number = int(input("Please enter the task number which of your task is complete :"))
            todos = functions.get_todos()
            removeTodoTask = todos[number]
            todos.pop(number)
            print(removeTodoTask, 'Removed from todos list')
            functions.write_todos(todos)
        case "exit":
            break
print("End of the program!")
