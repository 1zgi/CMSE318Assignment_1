from Student import Student
from FileOp import FileOp


class StudentService:
    __students_list = []

    def __init__(self):
        self.student = Student
        self.file = FileOp
        self.students = []  # List to store Student objects (max 100)
        self.next_student_number = 1  # Keeps track of the next available student number

    def add_student(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.__students_list.append(
            Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth))
        self.file.arrayToFile(self.__students_list)  # write student to the file


    @staticmethod
    def find_student_by_number(number):
        checker=True
        fileOpInstance = FileOp()
        students=fileOpInstance.readFromFile()
        for student in students:
            if student.get_student_number()==number:
                student.print_all_info()
                checker=False
        if checker:
            print("There is no record!")



    def modify_student(self, operation, student_num):
        self.find_student_by_number(student_num)
        if operation == "1":
            new_name = str(input("Enter new Name: "))
            self.student.set_first_name(new_name)

        if operation == "2":
            new_surname = str(input("Enter new Surname: "))
            self.student.set_last_name(new_surname)

        if operation == "3":
            new_date_of_birth = str(input("Enter new Date of birth: "))
            self.student.set_date_of_birth(new_date_of_birth)

        if operation == "4":
            new_sex = str(input("Enter new Sex: "))
            self.student.set_sex(new_sex)

        if operation == "5":
            new_country_of_birth = str(input("Enter new Country of Birth: "))
            self.student.set_country_of_birth(new_country_of_birth)

        if operation == "6":
            return False

    def find_by_birth_year(self,birth_year, students):
        self.file.readFromFile()
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