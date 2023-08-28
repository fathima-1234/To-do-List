import os
from datetime import datetime

tasks = []

def display_menu():
    print("=== To-Do List ===")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Edit Task")
    print("5. Exit")

def add_task():
    task_name = input("Enter the task name: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"name": task_name, "timestamp": timestamp})
    print("Task added successfully!")

def mark_completed():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} ({task['timestamp']})")
    task_num = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def view_tasks():
    print("=== Task List ===")
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['name']} ({task['timestamp']})")
    else:
        print("No tasks found.")

def edit_task():
    
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} ({task['timestamp']})")
    task_num = input("Enter the task number to edit: ")
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(tasks):
            new_task_name = input("Enter the new task name: ")
            tasks[task_num - 1]['name'] = new_task_name
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

        input("Press Enter to continue...")
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()