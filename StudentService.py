from Student import Student
from FileOp import FileOp


class StudentService:
    def __init__(self):
        self.student = Student
        self.file = FileOp
        self.students = []  # List to store Student objects (max 100)
        self.next_student_number = 1  # Keeps track of the next available student number

    def add_student(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        fileOpInstance=FileOp()
        students_list = []
        students_list.append(
            Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth))
        fileOpInstance.arrayToFile(students_list)  # write student to the file


    @staticmethod
    def find_student_by_number(number):
        checker=True
        fileOpInstance = FileOp()
        students=fileOpInstance.readFromFile()
        for student in students:
            if student.get_student_number()==number:
                return student
                checker=False
        if checker:
            print("There is no record!")



    def modify_student(self, operation, student_num):
        fileOpInstance = FileOp()
        student=self.find_student_by_number(student_num)
        if student==None:
            print("There is no student with "+student_num+" number")
        else:
            if operation == "1":
                new_name = input("Enter new Name: ")
                student.set_first_name(new_name)

            if operation == "2":
                new_surname = str(input("Enter new Surname: "))
                student.set_last_name(new_surname)

            if operation == "3":
                new_date_of_birth = str(input("Enter new Date of birth: "))
                student.set_date_of_birth(new_date_of_birth)

            if operation == "4":
                new_sex = str(input("Enter new Sex: "))
                student.set_sex(new_sex)

            if operation == "5":
                new_country_of_birth = str(input("Enter new Country of Birth: "))
                student.set_country_of_birth(new_country_of_birth)

            if operation == "6":
                return False
            fileOpInstance.deleteStudent(student_num)
            students=fileOpInstance.readFromFile()
            students.append(student)
            fileOpInstance.arrayToFileWriteMode(students)


    def find_by_birth_year(self,birth_year):
        file=FileOp()
        students=file.readFromFile()
        is_student_exist = False
        for student in students:
            if student.get_date_of_birth()[-4:] == birth_year:
                student.print_all_info()
                is_student_exist = True
        if not is_student_exist:
            print("There is no person in this birth date.")
    def show_all_students(self):
        fileOpInstance = FileOp()
        students=fileOpInstance.readFromFile()

        for student in students:
            student.print_all_info()