import os

tasks = []

def addTask():
    task = input("Enter task: ")
    tasks.append(task)
    os.system("clear")
    print(f"Task '{task}' added to the list!")

def listTasks():
    if not tasks:
        os.system("clear")
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            os.system("clear")
            print(f"Task #{index}. {task}")
            

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            os.system("clear")
            print(f"Task {taskToDelete} deleted successfully.")
        else:
            print(f"Task #{taskToDelete} was not found.") 
            
            
    except:
        print("Invalid input.")

if __name__ == "__main__":
    # main()
    print("Welcome to the To-Do List App!")

while True:
    print("\n")
    print("Please select an option:")
    print("----------------------------------------")
    print ("1. Add Task")
    print("2. Delete Task")
    print("3. List Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if(choice =="1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif(choice == "3"):
        listTasks()
    elif(choice == "4"):
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
