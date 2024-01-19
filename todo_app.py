def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the to-do list.")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("-----To-Do List-----")
        for i, task in enumerate(todo_list, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def complete_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["completed"] = True
        print(f"Task '{todo_list[task_index - 1]['task']}' marked as completed.")
    else:
        print("Invalid task index.")

def main():
    todo_list = []

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == '2':
            view_tasks(todo_list)2
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            complete_task(todo_list, task_index)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()
