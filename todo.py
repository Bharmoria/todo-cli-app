tasks = []

def show_tasks():
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid number.")

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
