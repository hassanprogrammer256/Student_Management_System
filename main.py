import tkinter as tk
from tkinter import messagebox, simpledialog
from constants import *
from System import *

class StudentManagementApp:
    def __init__(self, root, system):
        self.system = system
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        root.resizable(False, False) 
        root.config(bg=WHITE)
        root.title("Student Management System")
        
        # Add Student Button
        self.add_student_btn = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_student_btn.pack(pady=10)

        # View Students Button
        self.view_students_btn = tk.Button(root, text="View Students", command=self.view_students)
        self.view_students_btn.pack(pady=10)

        # Add Course Button
        self.add_course_btn = tk.Button(root, text="Add Course", command=self.add_course)
        self.add_course_btn.pack(pady=10)

    def add_student(self):
        student_id = simpledialog.askinteger("Input", "Enter Student ID:")
        name = simpledialog.askstring("Input", "Enter Name:")
        age = simpledialog.askinteger("Input", "Enter Age:")
        gender = simpledialog.askstring("Input", "Enter Gender:")
        student = Student(student_id, name, age, gender)
        self.system.add_student(student)
        messagebox.showinfo("Success", f"Student {name} added!")

    def view_students(self):
        students_info = [student.get_details() for student in self.system.students]
        messagebox.showinfo("Student List", "\n".join(students_info))

    def add_course(self):
        course_id = simpledialog.askinteger("Input", "Enter Course ID:")
        course_name = simpledialog.askstring("Input", "Enter Course Name:")
        credits = simpledialog.askinteger("Input", "Enter Credits:")
        course = Course(course_id, course_name, credits)
        self.system.add_course(course)
        messagebox.showinfo("Success", f"Course {course_name} added!")

if __name__ == "__main__":
    root = tk.Tk()
    system = StudentManagementSystem()
    app = StudentManagementApp(root, system)
    root.mainloop()