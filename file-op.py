from array import *
std1=["22450287","Ulas","Kilivan","30.10.1999","male","Turkey"]
std2=["17723499","Burak","Isaogullari","04.11.1999","male","Cyprus"]
std3=["22450367","Izgi","Kanatli","05.07.2000","male","Cyprus"]
std4=["22023255","Ahmet Eray","Alkan","05.04.2002","male","Turkey"]
students=list()

def arrayToFile(students):
    stdFile=open("students.txt","a")#file opened in append mode
    j=0
    stdString=""
    for student in students:
        for i in student:#Converts list to string and adds "-" between datas
            stdString+=student[j]+"-"
            j += 1
        stdString=stdString[:len(stdString)-1]+"%"#deletes unrelevant "-" sign and adds "%" sign for seperating students in file
        j=0
    stdString=stdString[:len(stdString)-1]#deletes unrelevant "&" sign
    stdFile.write(stdString)
    stdFile.close()
def readFromFile():
    stdFile=open("students.txt","r")
    stdString=stdFile.read()
    tempStudents=stdString.split("%")#splits students from eachother
    for student in tempStudents:
        tmpList=student.split("-")#splits students datas from eachother
        students.append(tmpList)
def deleteStudent(stdNum):
    readFromFile()
    j=0
    isNumExist=True#if number is not exist, second if condition will work
    for student in students:
        if student[0]==stdNum:#checks entered value
            students.pop(j)
            isNumExist=False
        j += 1
    if isNumExist:
        print("There is no student have this student number.")
