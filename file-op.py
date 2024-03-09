from array import *
from Student import Student
std1=Student("22450287","Ulas","Kilivan","30.10.1999","male","Turkey")
std2=Student("17723499","Burak","Isaogullari","04.11.1999","male","Cyprus")
std3=Student("22450367","Izgi","Kanatli","05.07.2000","male","Cyprus")
std4=Student("22023255","Ahmet Eray","Alkan","05.04.2002","male","Turkey")
#students=[std1,std2,std3,std4]
students=[]
def arrayToFile(students):
    stdFile=open("students.txt","a")#file opened in append mode
    stdString=""
    for student in students:
        stdString+=student.get_student_number()+"-"+student.get_first_name()+"-"+student.get_last_name()+"-"+student.get_date_of_birth()+"-"+student.get_sex()+"-"+student.get_country_of_birth()+"%"
    stdString=stdString[:len(stdString)-1]#deletes unrelevant "%" sign
    stdFile.write(stdString)
    stdFile.close()
def readFromFile():
    stdFile=open("students.txt","r")
    stdString=stdFile.read()
    tempStudents=stdString.split("%")#splits students from eachother
    for student in tempStudents:
        tmpList=student.split("-")#splits students datas from eachother
        tmpStd=Student(tmpList[0],tmpList[1],tmpList[2],tmpList[3],tmpList[4],tmpList[5])
        students.append(tmpStd)

def deleteStudent(stdNum):
    readFromFile()
    j=0
    isNumExist=True#if number is not exist, second if condition will work
    for student in students:
        if student.get_student_number()==stdNum:#checks entered value
            students.pop(j)
            isNumExist=False
        j += 1
    if isNumExist:
        print("There is no student have this student number.")