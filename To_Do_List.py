FILENAME = "tasks.txt"
tasks = []
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
def save_tasks():
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")
def add_task():
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty!")
def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def delete_task():
    if not tasks:
        print("No tasks to delete!")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("===========================")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye! Tasks saved.")
        break
    else:
        print("Invalid choice! Please enter 1–4.")
