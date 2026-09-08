import json

def show_menu():
    print("\n==== TASK MANAGER =====")
    print("1. : Add Task")
    print("2. : View Tasks")
    print("3. : Complete Task")
    print("4. : Delete Task")
    print("5. : Exit")


tasks = []
# show_menu()

def save_task_to_file():
    try:
        with open("task.json", "w") as file:
            json.dump(tasks, file, indent=4) #write task to a file 
    except Exception as e:
        print(f"Error saving Tasks: {e}")

def load_tasks_from_file():
    global tasks

    try:
        with open("task.json", "r") as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []

def add_task():
    task_title = input("Enter Task Title : ")
        
    # create new_task dictionary
    new_task = {
        "title" : task_title,
        "completed" : False
    }

    tasks.append(new_task)
    print("Added Successfully .")
    save_task_to_file()

def view_task():
    if not tasks:
            print("No Tasks yet! Add some task first")
    else:
        for i, task in enumerate(tasks, start=1):
            # Use ternary operator (instead of using if else condition and multiple line of code)
            status = "Completed" if task["completed"] else "Pending"
            print(i, ".", task["title"], status)
            print("*"*20)


def complete_task():
    for i, task in enumerate(tasks, start=1):

        print(i, ".", task['title'] )

    task_num = input("which task do you wanna mark complete : ")
    try:
        task_num = int(task_num)
    except ValueError:
        print("Enter a valid task number !")
        return
        # continue    # stops the current iteration and go back to the begining of the while loop.    

    if task_num<1 or task_num>len(tasks):
        print("Task not available for this number !")

    else:
        task = tasks[task_num -1]
        task['completed'] = True

        print("Title : ", task['title'])
        print("completed :", task["completed"])
        save_task_to_file()

def delete_task():
    for i, task in enumerate(tasks, start=1):
        print(i, ".", task['title'])
    print()

    task_num = input("Which task you wanna delete(Enter Number) : ")
    try:
        task_num = int(task_num)
    except ValueError:
        print("Enter a valid task number !")
        return

    if task_num<1 or task_num>len(tasks):
            print("Task not available for this number !")

    else:
        deleted_title = tasks[task_num -1]["title"]
        tasks.pop(task_num-1)
        print(f"✅ Task '{deleted_title}' deleted successfully!")
        save_task_to_file()

load_tasks_from_file()

while True:
    show_menu()

    choice = input("Enter Your choice : ")

    if choice == "1":
        print("Add Task Selected")
        print("*"*20)

        add_task()

    elif choice=="2":
        print("View Tasks Selected")
        print("*"*20)
        view_task()
                

    elif choice=="3":
        print("Complete Task Selected")
        print("*"*20)

        complete_task()

    elif choice=="4":
        print("Delete Task Selected")
        print("*"*20)

        delete_task()


    elif choice=="5":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")
        