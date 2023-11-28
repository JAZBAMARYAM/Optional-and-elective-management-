
class CourseManagement:
    def __init__(self):
        self.optional_courses = []
        self.elective_courses = []

    def add_optional_course(self, course_name):
        self.optional_courses.append(course_name)
        return f"{course_name} added to optional courses."

    def add_elective_course(self, course_name):
        self.elective_courses.append(course_name)
        return f"{course_name} added to elective courses."

    def view_optional_courses(self):
        return f"Optional Courses: {', '.join(self.optional_courses)}"

    def view_elective_courses(self):
        return f"Elective Courses: {', '.join(self.elective_courses)}"

# Example Usage:
course_manager = CourseManagement()
print(course_manager.add_optional_course("Computer Science"))
print(course_manager.add_elective_course("Data Science"))
print(course_manager.view_optional_courses())
print(course_manager.view_elective_courses())
