import os
import json

TASKS_FILE = 'tasks.json'

def loadTasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def saveTasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

tasks = loadTasks()

def addTask():
    task = input("Enter task (or type 'cancel' to go back): ").strip()
    if task.lower() == 'cancel':
        print("Add task operation cancelled.")
        return
    tasks.append(task)
    saveTasks()  
    os.system("clear")
    print(f"Task '{task}' added to the list!")


def listTasks():
    os.system("clear")
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    taskToDelete = input("Enter the # to delete (or type 'cancel' to go back): ").strip()
    if taskToDelete.lower() == 'cancel':
        os.system("clear")
        print("Delete task operation cancelled.")
        return
    try:
        taskToDelete = int(taskToDelete) - 1  
        if 0 <= taskToDelete < len(tasks):
            deleted_task = tasks.pop(taskToDelete)
            saveTasks()
            os.system("clear")
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print(f"Task #{taskToDelete + 1} was not found.")  
    except ValueError:
        os.system("clear")
        print("Invalid input.")
        
def deleteAllTasks():
    global tasks
    confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
    if confirm == 'yes':
        tasks.clear()
        saveTasks() 
        os.system("clear")
        print("All tasks have been deleted.")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    os.system("clear")
    print("Welcome to the To-Do List App!")
    
    while True:
        print("\n")
        print("Please select an option:")
        print("----------------------------------------")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Delete All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("clear")
            addTask()
        elif choice == "2":
            os.system("clear")
            deleteTask()
        elif choice == "3":
            os.system("clear")
            listTasks()
        elif choice == "4":
            os.system("clear")
            deleteAllTasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    os.system("clear")
    print("Goodbye!")
