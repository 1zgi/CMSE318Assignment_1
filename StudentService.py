from Student import *
from FileOp import *


class StudentService:
    students_list = [100]
    student = Student
    
    @staticmethod
    def add_student(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        self.students.append(student)
        FileOp.arrayToFile(self, student)

    def find_student_by_number(self, number):
        for student in self.student.get_student_number(number):
            if number == self.student.get_student_number(number):
                print(student.get_student_number())
