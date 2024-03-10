from StudentService import StudentService

system = StudentService()

print("Welcome to Student Information System!\nFunctions:\n1-Add a New Student\t\t2-Find a Student\n"
      "3-Show All Students\t\t4-Show Students by Birth Date\n5-Delete a Student\t\t6-Enter Whole Data to File\n"
      "7-Modify Student Information\n8-Get the Data From .txt to Array\n9-Quit")
choice = int(input("Type function's Number: "))


def switch(_choice):
    if _choice == 1:
        student_number = str(input("Student Number: "))
        first_name = str(input("First Name: "))
        last_name = str(input("Last Name: "))
        date_of_birth = str(input("Date of birth: "))
        sex = str(input("Sex: "))
        country_of_birth = str(input("Country of Birth: "))
        system.add_student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        return "Add a New Student"
    elif _choice == 2:
        student_id = input("Enter a student number to find: ")
        system.find_student_by_number(student_id)
        return "Find a Student"
    elif _choice == 3:
        system.show_all_students()
        return "Show All Students"
    elif _choice == 4:
        return "Show Students by Birth Date"
    elif _choice == 5:
        return "Delete a Student"
    elif _choice == 6:
        return "Enter Whole Data to File"
    elif _choice == 7:
        student_num = str(input("Enter a student number to modify: "))
        print("Which information would you like to change?"
              "1-Name   2-Surname\n"
              "3-Date of birth" "4-Sex:\n"
              "5-Country of Birth" "6-Exit")
        while True:
            operation = str(input("Type function's Number: "))
            system.modify_student(student_num, operation)
            return "Modify Student Information"
    elif _choice == 8:
        return "Get the Data From .txt to Array"
    elif _choice == 9:
        return "Quit"


switch(choice)
