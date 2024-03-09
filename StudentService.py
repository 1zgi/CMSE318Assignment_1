from Student import *


class StudentService:
    students_list = [100]
    student = Student

    @staticmethod
    def add_student(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        self.students.append(student)

    def find_student_by_number(self, number):
        for obj in self.student.get_student_number(number):
            if number == self.student.get_student_number(number):
                print(number)
