print("=" * 50)
print("          EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 50)

employees = []

while True:

    print("\n1: Add Employee")
    print("2: View Employees")
    print("3: Search Employee")
    print("4: Update Employee")
    print("5: Remove Employee")
    print("6: Exit")

    choice = input("Enter a choice: ")

    # Add Employee
    if choice == "1":
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        dep = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employee = {
            "name": name,
            "age": age,
            "department": dep,
            "salary": salary
        }

        employees.append(employee)
        print("Employee Added Successfully!")

    # View Employees
    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            print("\nNo. | Name | Age | Department | Salary")

            for index, employee in enumerate(employees, start=1):
                print(
                    index,
                    "|", employee["name"],
                    "|", employee["age"],
                    "|", employee["department"],
                    "|", employee["salary"]
                )

    # Search Employee
    elif choice == "3":
        employeeName = input("Enter Employee Name to Search: ")

        for employee in employees:
            if employee["name"] == employeeName:
                print("\nEmployee Found!")
                print("Name:", employee["name"])
                print("Age:", employee["age"])
                print("Department:", employee["department"])
                print("Salary:", employee["salary"])
                break
        else:
            print("Employee not found.")

    # Update Employee
    elif choice == "4":
        employeeName = input("Enter Employee Name to Update: ")

        for employee in employees:
            if employee["name"] == employeeName:

                employee["name"] = input("Enter New Name: ")
                employee["age"] = int(input("Enter New Age: "))
                employee["department"] = input("Enter New Department: ")
                employee["salary"] = float(input("Enter New Salary: "))

                print("Employee Updated Successfully!")
                break
        else:
            print("Employee not found.")

    # Remove Employee
    elif choice == "5":
        employeeName = input("Enter Employee Name to Remove: ")

        for employee in employees:
            if employee["name"] == employeeName:
                employees.remove(employee)
                print("Employee Removed Successfully!")
                break
        else:
            print("Employee not found.")

    # Exit
    elif choice == "6":
        print("Exiting Employee Management System...")
        break

    else:
        print("Invalid choice. Please try again.")