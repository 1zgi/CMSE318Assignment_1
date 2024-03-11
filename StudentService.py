from Student import Student
from FileOp import FileOp


class StudentService:
    def __init__(self):#other classes defined for using in this class
        self.student = Student
        self.file = FileOp()

    def add_student(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        students_list = []
        students_list.append(
            Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth))
        self.file.arrayToFile(students_list)  # write student to the file

    def find_student_by_number(self,number):
        checker=True
        students=self.file.readFromFile()#reads the latest version of file
        for student in students:
            if student.get_student_number()==number:#checks every student by student number if there is a match
                return student
        if checker:#if inside the for loop, if condition not satisfied, prints the following
            print("There is no record!")

    def modify_student(self, operation, student_num):
        student=self.find_student_by_number(student_num)#finds the student from the file by number
        if student==None:#if there is a student by that number...
            print("There is no student with "+student_num+" number")
        else:#simply by the chosen option information updated with setters
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
            self.file.deleteStudent(student_num)#old record deleted
            students=self.file.readFromFile()#new version taken from file
            students.append(student)#updated version appended to taken array
            self.file.arrayToFileWriteMode(students)#fully updated list saved to txt


    def find_by_birth_year(self,birth_year):
        students=self.file.readFromFile()#last version gathered
        is_student_exist = False
        for student in students:
            if student.get_date_of_birth()[-4:] == birth_year:#last for digit means birth year
                student.print_all_info()
                is_student_exist = True
        if not is_student_exist:#with is_student_exist variable we check if not information message printed
            print("There is no person in this birth date.")
    def show_all_students(self):
        students=self.file.readFromFile()#updated version gathered
        for student in students:#printed one by one
            student.print_all_info()
            print()