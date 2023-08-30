# Final Project Attendance System
Name ="mohammed Emad Hamoda"
Delivery_Date = "29/8/2023"


import uuid
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_student_count = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_student_count += 1

        def enroll_course(self, course_name, course_mark):
            course = Course(course_name, course_mark)
            self.courses_list.append(course)

        def get_student_details(self):
            return self.__dict__

        def get_student_courses(self):
            for course in self.courses_list:
                print(f"Course: {course.course_name}, Mark: {course.course_mark}")

        def get_student_average(self):
            if len(self.courses_list) == 0:
                return 0
            total_marks = sum(course.course_mark for course in self.courses_list)
            return total_marks / len(self.courses_list)
