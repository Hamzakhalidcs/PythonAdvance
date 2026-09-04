def show_menu():
    print("\n==== TASK MANAGER =====")
    print("1. : Add Task")
    print("2. : View Tasks")
    print("3. : Complete Task")
    print("4. : Delete Task")
    print("5. : Exit")


tasks = []
# show_menu()

while True:
    show_menu()

    choice = input("Enter Your choice : ")

    if choice == "1":
        print("Add Task Selected")
        print("*"*20)

        task_title = input("Enter Task Title : ")
        
        # create new_task dictionary
        new_task = {
            "title" : task_title,
            "completed" : False
        }

        tasks.append(new_task)
        print("Added Successfully .")

    elif choice=="2":
        print("View Tasks Selected")
        print("*"*20)

        if not tasks:
            print("No Tasks yet! Add some task first")
        else:
            for task in tasks:
                print("Title :", task["title"])
                print("Completed :",task["completed"])
                print("*"*20)
                

    elif choice=="3":
        print("Complete Task Selected")
        print("*"*20)

        task_num = input("which task do you wanna mark complete : ")
        task_num = int(task_num)
        
        if task_num<1 or task_num>len(tasks):
            print("Task not available for this number !")

        else:
            task = tasks[task_num -1]
            task['completed'] = True

            print("Title : ", task['title'])
            print("completed :", task["completed"])


    elif choice=="4":
        print("Delete Task Selected")
        print("*"*20)

        task_num = input("Which task you wanna delete(Enter Number) : ")
        if task_num.isdigit():
            task_num = int(task_num)
            if task_num<1 or task_num>len(tasks):
                print("Task not available for this numbers !")

            else:
                deleted_title = tasks[task_num -1]["title"]
                tasks.pop(task_num-1)
                print(f"✅ Task '{deleted_title}' deleted successfully!")



    elif choice=="5":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")
        