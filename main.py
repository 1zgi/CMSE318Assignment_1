from StudentService import StudentService

print("Welcome to Student Information System!\nFunctions:\n1-Add a New Student\t\t2-Find a Student\n"
      "3-Show All Students\t\t4-Show Students by Birth Date\n5-Delete a Student\t\t6-Enter Whole Data to File\n"
      "7-Modify Student Information\n8-Get the Data From .txt to Array\n9-Quit")
choice = int(input("Type function's Number: "))


def switch(_choice):
    if _choice == 1:
        return "Add a New Student"
    elif _choice == 2:
        return "Find a Student"
    elif _choice == 3:
        return "Show All Students"
    elif _choice == 4:
        return "Show Students by Birth Date"
    elif _choice == 5:
        return "Delete a Student"
    elif _choice == 6:
        return "Enter Whole Data to File"
    elif _choice == 7:
        return "Modify Student Information"
    elif _choice == 8:
        return "Get the Data From .txt to Array"
    elif _choice == 9:
        return "Quit"


switch(choice)
