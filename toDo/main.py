import os
import json

TASKS_FILE = 'tasks.json'
COMPLETED_TASKS_FILE = 'completed_tasks.json'

def loadTasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def saveTasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

tasks = loadTasks(TASKS_FILE)
completed_tasks = loadTasks(COMPLETED_TASKS_FILE)

def addTask():
    task = input("Enter task (or type 'cancel' to go back): ").strip()
    if task.lower() == 'cancel':
        print("Add task operation cancelled.")
        return
    tasks.append(task)
    saveTasks(TASKS_FILE, tasks)
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

def listCompletedTasks():
    os.system("clear")
    if not completed_tasks:
        print("There are no completed tasks currently.")
    else:
        print("Completed Tasks:")
        for index, task in enumerate(completed_tasks, start=1):
            print(f"Completed Task #{index}. {task}")

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
            saveTasks(TASKS_FILE, tasks)
            os.system("clear")
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print(f"Task #{taskToDelete + 1} was not found.")
    except ValueError:
        os.system("clear")
        print("Invalid input.")

def completeTask():
    listTasks()
    taskToComplete = input("Enter the # of the task to mark as completed (or type 'cancel' to go back): ").strip()
    if taskToComplete.lower() == 'cancel':
        os.system("clear")
        print("Complete task operation cancelled.")
        return
    try:
        taskToComplete = int(taskToComplete) - 1
        if 0 <= taskToComplete < len(tasks):
            completed_task = tasks.pop(taskToComplete)
            completed_tasks.append(completed_task)
            saveTasks(TASKS_FILE, tasks)
            saveTasks(COMPLETED_TASKS_FILE, completed_tasks)
            os.system("clear")
            print(f"Task '{completed_task}' marked as completed and moved to completed tasks list.")
        else:
            print(f"Task #{taskToComplete + 1} was not found.")
    except ValueError:
        os.system("clear")
        print("Invalid input.")

if __name__ == "__main__":
    os.system("clear")
    print("Welcome Michael!")
    
    while True:
        print("\n")
        print("Please select an option:")
        print("----------------------------------------")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Complete Task")  
        print("5. List Completed Tasks") 
        print("6. Exit")

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
            completeTask()
        elif choice == "5":  
            os.system("clear")
            listCompletedTasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    os.system("clear")
    print("Goodbye!")