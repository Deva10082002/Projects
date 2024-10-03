import time
import getpass
import tkinter as tk
from tkinter import simpledialog
class Student:
    def __init__(self, student_id, name, age, grades):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades
        #self.usernmae=username
        #self.password=passwword

    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, GPA: {self.calculate_gpa():.2f}"


students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    grades = list(map(int, input("Enter Student Grades: ").split(',')))

    new_student = Student(student_id, name, age, grades)
    students.append(new_student)
    print("Student added successfully!")


def display_students():
    if not students:
        print("No students to display.")
        return

    for student in students:
        print(student)


def update_student():
    student_id = input("Enter the Student ID to update: ")
    for student in students:
        if student.student_id == student_id:
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.grades = list(map(int, input("Enter new grades (comma-separated): ").split(',')))
            print("Student record updated successfully!")
            return
    print("Student ID not found.")


def delete_student():
    student_id = input("Enter the Student ID to delete: ")
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student record deleted successfully!")
            return
    print("Student ID not found.")


def search_student():
    student_id = input("Enter the Student ID to search: ")
    for student in students:
        if student.student_id == student_id:
            print(student)
            return
    print("Student ID not found.")


def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose again.")

count=3
username = "DEVA"
passsword = "deva"
m = input("Enter the username:")
password = input("Enter the password:")
while count > 0:
    if password == passsword and m == username:
        if __name__ == "__main__":
            main_menu()
    elif password != passsword and m != username:
        print("Invalid password and Invalid password")
        print("Only ", count, "times left")
        count -= 1
        break
    elif password == passsword and m != username:
        print("Invalid username")
        print("Only ", count, "times left")
        count -= 1
        break
    elif password != password and m == username:
        print("Invalid password")
        print("Only ", count, "times left")
        count -= 1
        break

else:
    print("Temporarily blocked")
    print("Wait for 10 seconds")
    time.sleep(10)
    count = 3







