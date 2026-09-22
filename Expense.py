print("======== Expense Tracker ========")

expenses = []
while True:
    print("1: Add Expense")
    print("2: View Expense")
    print("3: Calculate Total")
    print("4: Remove Expense")
    print("5: Exit")

    choice = input("Enter a choice:")

    if choice == "1":
        add = input("Enter an Expense name: ")
        amount = float(input("Enter amount: "))
        expense = {
        "name" : add,
        "Amount" : amount
    }
        expenses.append(expense)
    elif choice == "2":
        for index, expense in enumerate(expenses, start = 1):
            print(index, expense["name"], "-", expense["Amount"])

    elif choice == "3":
        totalsum = 0
        for expense in expenses:
            totalsum = totalsum + expense["Amount"]
        print("Total Expense: ", totalsum)
    elif choice == "4":
        remove = int(input("Enter expense to remove: "))
        expenses.pop(remove - 1)
        print("Expense Remove successfully")
    elif choice == "5":
        break