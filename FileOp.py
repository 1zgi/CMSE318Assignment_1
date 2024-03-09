from Student import Student
class FileOp:
    def arrayToFile(self,students):
        stdFile=open("students.txt","a")#file opened in append mode
        stdString=""
        for student in students:
            stdString+=student.get_student_number()+"-"+student.get_first_name()+"-"+student.get_last_name()+"-"+student.get_date_of_birth()+"-"+student.get_sex()+"-"+student.get_country_of_birth()+"%"
        stdString=stdString[:len(stdString)-1]#deletes unrelevant "%" sign
        stdFile.write(stdString)
        stdFile.close()
    def readFromFile(self):
        students=[]
        stdFile=open("students.txt","r")
        stdString=stdFile.read()
        tempStudents=stdString.split("%")#splits students from eachother
        for student in tempStudents:
            tmpList=student.split("-")#splits students datas from eachother
            tmpStd=Student(tmpList[0],tmpList[1],tmpList[2],tmpList[3],tmpList[4],tmpList[5])
            students.append(tmpStd)
        return students
    def deleteStudent(self,stdNum,students):
        self.readFromFile()
        j=0
        isNumExist=True#if number is not exist, second if condition will work
        for student in students:
            if student.get_student_number()==stdNum:#checks entered value
                students.pop(j)
                isNumExist=False
            j += 1
        if isNumExist:
            print("There is no student have this student number.")

    def findByBirthYear(self,birthYear,students):
        self.readFromFile()
        isStudentExist=False
        for student in students:
            if(student.get_date_of_birth()[-4:]==birthYear):
                student.print_all_info()
                isStudentExist=True
        if not isStudentExist:
            print("There is no person in this birth date.")
    def getValue(self):#Asks user to be sure about entered data and sends if user sure
        while True:
            temp = input("Please enter new data: ")
            while True:#only way to out is confirming entered value
                check = int(input("Entered data is " + temp + "\nConfirm(1/0): "))
                if check == 1:
                    return temp
                elif check == 0:
                    break
                else:
                    print("You can only enter 1 or 0 for confirmation!")
    def modifyStudent(self,stdNum,students):
        for student in students:
            if(student.get_student_number()==stdNum):
                print("Which information would you like to change?\n"
                      "1-Name           2-Surname\n"
                      "3-Birth Date     4-Gender\n"
                      "5-Country of Birth")
                choice=int(input("Please enter the number of your choice: "))
                while True:
                    if choice==1:
                        student.set_first_name(self.getValue())
                        print("Data entered succesfully! Updated version:\n")
                        student.print_all_info()
                        break
                    elif choice==2:
                        student.set_last_name(self.getValue())
                        print("Data entered succesfully! Updated version:\n")
                        student.print_all_info()
                        break
                    elif choice==3:
                        student.set_date_of_birth(self.getValue())
                        print("Data entered succesfully! Updated version:\n")
                        student.print_all_info()
                        break
                    elif choice==4:
                        student.set_sex(self.getValue())
                        print("Data entered succesfully! Updated version:\n")
                        student.print_all_info()
                        break
                    elif choice==5:
                        student.set_country_of_birth(self.getValue())
                        print("Data entered succesfully! Updated version:\n")
                        student.print_all_info()
                        break
                    else:
                        print("Please enter valid value between 1-5")