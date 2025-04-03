class Instructor:
    def __init__(self, instructor_id, name, department):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department

    def teach_course(self, course):
        return f"{self.name} teaches {course.course_name}"

    def get_details(self):
        return f"{self.name}, Department: {self.department}"