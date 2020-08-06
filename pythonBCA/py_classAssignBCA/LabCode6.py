import datetime

class Student:
    def __init__(self, regno, name):
        self.regno=regno
        self.name=name
        self.attn_per=0
        self.attendance=dict()
        self.class_conducted=dict()
    def display(self):
        print("{}\t{}\t{}".format(self.regno, self.name, self.attn_per))

class Marks(Student):
    def __init__(self,regno, name):
        Student.__init__(self, regno, name)
        self.mark=dict()

students=[]
s_name=[]
s_code=[]
flag=0
c2=0
ch='y'
while ch=='y' or ch=='Y':
    if(flag==0):
        flag=1
        print("Lab 5 Python")
        print("\nMishan Regmi 1841030 5 BCA 'A'\n")
        print("Lets Start With Some Detail First")
        course=input("\n1. Course name : ")
        sem=input("\n2. Semester : ")
        no_courses=int(input("\n3. Number of subjects : "))
        for i in range(0,no_courses):
             s_name.append(input("\nEnter the subject name : "))
             s_code.append(input("\nEnter the subject code : "))
        n=int(input("\n\nNo of students in {}-{} : ".format(sem,course)))
        for i in range(0,n):
            regno=input("\nRoll No : ")
            name=input("Student Name : ")
            students.append(Marks(regno,name))
            for temp in s_code:
                students[i].attendance[temp]=0
                students[i].class_conducted[temp]=0

    print("\n\nMain Menu:\n1. Attendance\n2. Exams\n3. Student Details\n4. Course details\n5. Time Table\n6. Exit")
    ch1=int(input("\nEnter choice : "))
    if(ch1==1):
        print("\n\nAttendance-Menu:\n 1. Log Attendance\n 2. Display Attendance\n 3. Back to Main Menu")
        ch2=int(input("\nEnter choice : "))
        if(ch2==1):
            print("\nSelect the subject from below :")
            for i in range(0, no_courses):
                print("{} - {}".format(s_code[i],s_name[i]))
            code=input("\nEnter the subject code : ")
            print("\n\nEnter 'P' for present and 'AB' for absent --->\n\n")
            for i in range(0,n):
                temp=input("{} - ".format(students[i].regno))
                students[i].class_conducted[code]+=1
                if(temp=='p' or temp=='P'):
                    students[i].attendance[code]+=1
        elif(ch2==2):
            t_no=input("Enter Register Number : ")
            for i in range(0,n):
                if students[i].regno==t_no :
                    sum_per=0
                    print("\n\n\tAttendance Sheet\n\n")
                    print(" Name : {}\tRegister Number : {}".format(students[i].name,students[i].regno))
                    print("\n\n\nSubject Name\tSubject Code\tConducted\tPresent\t\tPercentage\n\n")
                    for j in range(0,no_courses):
                        a=students[i].class_conducted[s_code[j]]
                        b=students[i].attendance[s_code[j]]
                        if(a==0):
                            per=0
                        else:
                            per=(b/a)*100
                        sum_per+=per
                        print("{}\t\t{}\t\t{}\t\t{}\t\t{:.2f}".format(s_name[j],s_code[j],a,b,per))
                    new_tot=(sum_per/(no_courses*100))*100
                    print("\n\nTotal percentage = {:.2f}%".format(new_tot))
                    if(new_tot<80):
                        print("\n\nYour Attendance is very low (less than 80%)\n\n")
        elif(ch2==3):
            continue
    elif(ch1==2):
        print("\n\nExams-Menu:\n 1. Generate Timetable\n 2. Update Marks\n 3. Display Marksheet\n 4.Back to Main Menu")
        ch3=int(input("\nEnter choice : "))
        if(ch3==1):
            date_entry = input('\n\n Enter start date of exam (in YYYY-MM-DD format) : ')
            year, month, day = map(int, date_entry.split('-'))
            print("\n\n\n\t\t**Exam Schedule**")
            print("\n\n\tDate\t\tSubject Code\tSubject Name\n")
            date1 = datetime.date(year, month, day)
            for i in range(0, no_courses):
                print("\t{}\t{}\t\t{}".format(date1,s_code[i],s_name[i]))
                date1=date1+datetime.timedelta(days=2)
        elif(ch3==2):
            k=0
            print("\n\n    Marks Sheet\n\n")
            print("Enter marks for each student below---->\n")
            for i in range(0,n):
                print("\nReg No : {}\t Name : {}\n".format(students[i].regno,students[i].name))
                for temp in s_name:
                    mark_temp=int(input("{} - ".format(temp)))
                    retest=input("Was it a re-exam?(y/n) : ")
                    if(retest=='y' or retest=='Y'):
                        students[i].mark[temp]=mark_temp-(0.1*mark_temp)
                    else:
                        students[i].mark[temp]=mark_temp
        elif(ch3==3):
            t_no=input("Enter Register Number : ")
            for i in range(0,n):
                if students[i].regno==t_no :
                    sum=0
                    print("\n\n\tMark Sheet\n\n")
                    print(" Name : {}\tRegister Number : {}".format(students[i].name,students[i].regno))
                    print("\n\n\nSubject Name\tSubject Code\tMax Marks\tMarks Awarded\n\n")
                    for j in range(0,no_courses):
                        a=100
                        b=students[i].mark[s_name[j]]
                        sum+=b
                        print("{}\t\t{}\t\t{}\t\t{}".format(s_name[j],s_code[j],a,b))
                    new_tot=(sum/(no_courses*100))*100
                    print("\n\n  Total Percentage :{:.2f}%".format(new_tot))
                    if(new_tot<40):
                        print("\n\nYou have failed! You need to appear for supplementary exam...\n\n")
        elif(ch3==4):
            continue

    elif(ch1==3):
        print("\n\nReg No.\tName\tAttendance %")
        for student in students:
            student.display()
    elif(ch1==4):
        print("\n\nCourse Details :\n")
        for i in range(0, no_courses):
            print("{} - {}".format(s_code[i],s_name[i]))
    elif(ch1==5):
        print("\n\t******TIME TABLE*****\n") 
        print("\t  DATE\t\t\tSUBJECT")
        print("\t 4.8.2020\t\t{}".format(s_name[0]))
        print("\t 7.8.2020\t\t{}".format(s_name[1]))
        print("\t 4.8.2020\t\t{}".format(s_name[2]))
        print("\t 7.8.2020\t\t{}".format(s_name[3]))
        print("\n\t**********************\n")        
    elif(ch1==6):
        break
    ch=input("\nDo you want to continue?\n{Press 'y' to continue, Anything else to exit} : ")