class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def get_course_info(self):
        return f"{self.course_name}, Credits: {self.credits}, Enrolled: {[student.name for student in self.students]}"
