tasks = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter a choice:")

    if choice =="1":
        task = input("Enter a task:")
        tasks.append(task)
    elif choice == "2":
        for index, task in enumerate(tasks, start=1):
            print(index, task)
    elif choice == "3":
        remover = int(input("Which task want to remove:"))
        tasks.pop(remover - 1)
        print("Task remove successfully")
    elif choice == "4":
        break