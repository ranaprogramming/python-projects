import json

print("=" * 50)
print("          STUDENT MANAGEMENT SYSTEM")
print("=" * 50)


class Student:
    def __init__(self, name, age, student_id, marks):
        self.name = name
        self.age = age
        self.student_id = student_id
        self._marks = marks

    def display_info(self):
        return f"Student Name: {self.name} Student Age: {self.age} Student ID: {self.student_id} Student Marks: {self.marks}"

    def calculate_percentage(self):
        total = int(input("Enter Total Marks: "))
        percentage = (self.marks / total) * 100
        return percentage

    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    @staticmethod
    def validate_marks(marks, total):
        if marks < 0 or marks > total:
            return False
        return True

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Marks cannot be negative")
        else:
            self._marks = value

    @classmethod
    def create_student(cls, name, age, student_id, marks):
        return cls(name, age, student_id, marks)

    def __str__(self):
        return f"Student: {self.name} | Age: {self.age} | ID: {self.student_id} | Marks: {self.marks}"


def save_students():
    data = []

    for student in students:
        data.append({
            "Name": student.name,
            "Age": student.age,
            "Student_id": student.student_id,
            "Marks": student.marks
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Students saved successfully!")


def load_students():
    students = []

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        for student_data in data:
            student = Student(
                student_data["Name"],
                student_data["Age"],
                student_data["Student_id"],
                student_data["Marks"]
            )
            students.append(student)

    except FileNotFoundError:
        print("No saved student data found. Starting fresh.")

    return students


students = load_students()


while True:
    print("\n1: Add Student")
    print("2: View Students")
    print("3: Search Student")
    print("4: Update Student")
    print("5: Remove Student")
    print("6: Check Student Marks")
    print("7: Check Student Grade")
    print("8: Exit")

    choice = input("Enter a Choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        student_id = int(input("Enter Student ID: "))
        marks = int(input("Enter Student Marks: "))
        total = int(input("Enter Total Marks: "))

        if Student.validate_marks(marks, total):
            student = Student(name, age, student_id, marks)
            students.append(student)
            print("Student added successfully!")
        else:
            print("Invalid Marks")
    elif choice == "2":
        if len(students) == 0:
            print("No student found")
        else:
            for student in students:
                print(student.display_info())

    elif choice == "3":
        student_name = input("Enter Student Name: ")
        for student in students:
            if student.name == student_name:
                print(student.display_info())
                break
        else:
            print("No Student found")

    elif choice == "4":
        student_name = input("Enter Student Name: ")
        for student in students:
            if student.name == student_name:
                student.name = input("Enter new Name: ")
                student.age = int(input("Enter new age: "))
                student.student_id = int(input("Enter new student ID: "))

                print("Student Updated Successfully")
                break
        else:
            print("No Student found")

    elif choice == "5":
        student_name = input("Enter Student Name: ")
        for student in students:
            if student.name == student_name:
                students.remove(student)
                print("Student Removed successfully")
                break
        else:
            print("No Student found")

    elif choice == "6":
        student_name = input("Enter Student Name: ")
        for student in students:
            if student.name == student_name:
                print("Student Marks:", student.marks)
                percentage = student.calculate_percentage()
                print(f"Percentage: {percentage:.2f}%")
                break
        else:
            print("No Student found")
    elif choice == "7":
        student_name = input("Enter Student Name: ")
        for student in students:
            if student.name == student_name:
                print("Student Marks:", student.marks)
                percentage = student.calculate_percentage()
                print(f"Percentage: {percentage:.2f}%")
                grade = student.calculate_grade(percentage)
                print(f"Grade: {grade}")
                break
        else:
            print("No Student found")
    elif choice == "8":
        save_students()
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid Choice")