class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.instructors = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def add_course(self, course):
        self.courses.append(course)

    def get_student_info(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.get_details()
        return "Student not found"