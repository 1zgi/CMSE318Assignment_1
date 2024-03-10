from array import *
from Student import Student
class FileOp:
    def arrayToFile(students):
        stdFile=open("students.txt","a")#file opened in append mode
        stdString=""
        for student in students:
            stdString+=student.get_student_number()+"-"+student.get_first_name()+"-"+student.get_last_name()+"-"+student.get_date_of_birth()+"-"+student.get_sex()+"-"+student.get_country_of_birth()+"%"
        stdFile.write(stdString)
        stdFile.close()
    def readFromFile(self):
        students = []
        stdFile=open("students.txt","r")
        stdString=stdFile.read()
        stdString=stdString[:-1]
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
    def modifyStudent(self,stdNum,students):
        for student in students:
            if(student.get_student_number()==stdNum):
                print("Which information would you like to change?"
                      "1-Name   2-Surname\n"
                      "3-")

