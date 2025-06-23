# Simple To-Do List App

tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
