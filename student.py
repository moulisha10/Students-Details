import json
import os
class Student:
    def __init__(self, name, age, address, education):
        self.name=name
        self.age=age
        self.address=address
        self.education=education
    def to_dict(self):
        return{
            "name":self.name,
            "age":self.age,
            "address":self.address,
            "education":self.education,
        }
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename=filename
        self.students=self.load_students()
    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return[]
    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)
    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully")
    def display_all_students(self):
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students:
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Address: {student['address']}")
                print(f"Education: {student['education']}")
                print("-" * 30)
    def update_student(self,name):
        for student in self.students:
            if student["name"].lower()==name.lower():
                student["age"]=input("Enter new age")
                student["address"]=input("Enter new address")
                student["education"]=input("Enter new education")
                self.save_students()
                print("Student Information Updated Successfully")
                return
        print(f" No student found with name'{name}'.")
def main():
    manager=StudentManager()
    while True:
        print("\n1.Add Student")
        print("2. Display All Students")
        print("3. Update Student")
        print("4. Exit")
        choice=input("Enter your choice")
        if choice=='1':
            name=input("Enter student's name")
            age=input("Enter student's age")
            address=input("Enter student's address")
            education=input("Enter student's education")
            student=Student(name, age, address, education)
            manager.add_student(student)
        elif choice=='2':
            manager.display_all_students()
        elif choice=='3':
            name=input("Enter the name of the student to update")
            manager.update_student(name)
        elif choice=='4':
            print("Exiting program. Data saved in students.json.")
            break
        else:
            print("Invalid choice. Please Try Again")
if __name__ == "__main__":
    main()
