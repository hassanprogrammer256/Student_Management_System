class Student:
    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.courses = []
    
    def register_course(self, course):
        self.courses.append(course)
        course.add_student(self)
    
    def drop_course(self, course):
        self.courses.remove(course)
        course.remove_student(self)

    def get_details(self):
        return f"{self.name}, {self.age}, {self.gender}, Enrolled in: {[course.course_name for course in self.courses]}"

