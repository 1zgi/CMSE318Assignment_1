from Student import *


class StudentService:
    def __init__(self):
        self.students = []

    @staticmethod
    def add_student(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        self.students.append(student)
