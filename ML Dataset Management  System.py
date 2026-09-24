print("=" * 50)
print("             AI/ML Dataset Management System")
print("=" * 50)
import json
students = []

def view_data():
    if len(students) == 0:
        print("No data found")
    else:
        for data in students:
            print(f"Name: {data['name']} | Age: {data['age']} | Marks: {data['marks']}")

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Student age: "))
    marks = int(input("Enter Student marks: "))
    student ={
                    "name":name,
                    "age": age,
                    "marks": marks
                    }
    students.append(student)
    print("Student Added Successfully")
def search_student():
    student_name = input("Enter student name: ")
    for data in students:
        if data["name"] == student_name:
            print(f"Name: {data['name']} | Age: {data['age']} | Marks: {data['marks']}")
            break
    else:
        print("No student found")

def update_data():
    student_name = input("Enter student name: ")
    for data in students:
        if data["name"] == student_name:
            new_age = int(input("Enter new age: "))
            new_marks = int(input("Enter new marks: "))
            data["age"] = new_age
            data["marks"] = new_marks
            print("Student Data Updated successfully")
            break
    else:
        print("No student found")
def delete_data():
    student_name = input("Enter student name: ")
    for data in students:
        if data["name"] == student_name:
            students.remove(data)
            print("Student Data Removed successfully")
            break
    else:
        print("No student found")

def dataset_statistics():
        marks = []
        print(f"Total Students: {len(students)}")
        for data in students:
            marks.append(data["marks"])
        
        average = sum(marks) / len(marks)
        print(f"Average Marks: {average}")

        highest = max(marks)
        print(f"Highest Marks: {highest}")

        lowest = min(marks)
        print(f"Lowest Marks: {lowest}")

def save_data():
    with open("studentsdata.json", "w") as file:
        json.dump(students, file, indent = 4)
    print("Data saved successfully")
def load_data():
    with open("studentsdata.json", "r") as file:
            data = json.load(file)
    students.clear()
    students.extend(data)

    print("Data loaded successfully")

load_data()
while True:
    print("1. View Data")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Dataset Statistics")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_data()
    elif choice == "2":
            add_student()
    elif choice == "3":
            search_student()
    elif choice == "4":
            update_data()
    elif choice == "5":
            delete_data()
    elif choice == "6":
            dataset_statistics()
    elif choice == "7":
            save_data()
    elif choice == "8":
            load_data()
    elif choice == "9":
        break