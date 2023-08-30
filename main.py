# Final Project Attendance System
Name ="mohammed Emad Hamoda"
Delivery_Date = "29/8/2023"

import csv
import datetime
def mark_attendance(student_id):
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, current_date, current_time])

    print("Attendance marked successfully!")


def main():
    print("ITF 07 Final Project Attendance System")

    student_id = input("Enter student ID: ")
    mark_attendance(student_id)


if __name__ == "__main__":
    main()

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

students = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))
    except ValueError:
        print("Invalid selection. Please enter a number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value")
        student = Student(student_name, student_age, student_number)
        students.append(student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                students.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                print("Student Details:")
                print(f"Student ID: {student.student_id}")
                print(f"Student Name: {student.student_name}")
                print(f"Student Age: {student.student_age}")
                print(f"Student Number: {student.student_number}")
                print("Courses:")
                student.get_student_courses()
                break
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                average = student.get_student_average()
                print(f"Student Average: {average}")
                break
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                while True:
                    try:
                        course_mark = float(input("Enter Course Mark: "))
                        break
                    except ValueError:
                        print("Invalid Value")
                student.enroll_course(course_name, course_mark)
                print("Course Added Successfully")
                break

