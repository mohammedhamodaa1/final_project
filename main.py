# Final Project Attendance System
Name ="mohammed Emad Hamoda"
Delivery_Date = "29/8/2023"

import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark