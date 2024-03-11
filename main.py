from StudentService import StudentService
from FileOp import FileOp
system = StudentService()
file=FileOp()
students=[]#list defined globally for file i/o purposes
print("Welcome to Student Information System!")
def switch():#for organizing every option in one method
    print("Functions:\n1-Add a New Student\t\t2-Find a Student\n"
          "3-Show All Students\t\t4-Show Students by Birth Date\n5-Delete a Student\t\t6-Modify Student Information\n"
          "7-Get the Data From .txt to Array\n8-Quit")
    choice = int(input("Type function's Number: "))
    if choice == 1:#inputs taken and sent with calling add student method
        student_number = str(input("Student Number: "))
        first_name = str(input("First Name: "))
        last_name = str(input("Last Name: "))
        date_of_birth = str(input("Date of birth: "))
        sex = str(input("Sex: "))
        country_of_birth = str(input("Country of Birth: "))
        system.add_student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
        print("Student added successfully!")

    elif choice == 2:
        student_id = input("Enter a student number to find: ")
        student=system.find_student_by_number(student_id)
        if student!=None:
            student.print_all_info()
        else:
            print("No information with this student number")
    elif choice == 3:
        system.show_all_students()
    elif choice == 4:
        birthDate=input("Please enter birth date: ")
        system.find_by_birth_year(birthDate)
    elif choice == 5:
        stdNum=input("Enter the number of the student you want to delete: ")
        student = system.find_student_by_number(stdNum)
        print("Student with following information deleted from file.")
        student.print_all_info()
        file.deleteStudent(stdNum)
    elif choice == 6:
        while True:
            student_num = str(input("Enter a student number to modify: "))
            print("Which information would you like to change?\n"
                  "1-Name              2-Surname\n"
                  "3-Date of birth     4-Sex:\n"
                  "5-Country of Birth  6-Exit")
            choice=input("Please enter your choice: ")
            if int(choice)>0 or int(choice)<7:
                system.modify_student(choice,student_num)
                print("Updated successfully!")
                break
            else:
                print("Please enter valid number")
    elif choice == 7:
        students=file.readFromFile()
        print("Students saved to list successfully!")
        print(students)
    elif choice == 8:
        print("Thank you for using our software!")
        exit()
while True:
    switch()
    choice=int(input("Would you like to do another operation?(1/0): "))
    if choice==1:
        switch()
    elif choice==0:
        print("Thank you for using our software!")
        exit()
    else:
        print("Please enter 1 or 0 only")