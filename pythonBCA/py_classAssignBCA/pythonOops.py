class Employee:  
    id = 10;  
    name = "Mishan"  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp = Employee()  
emp.display()  

class Employee:  
    def __init__(self,name,id):  
        self.id = id;  
        self.name = name;  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp1 = Employee("Mishan",101)  
emp2 = Employee("Regmi",102)  
  
#accessing display() method to print employee 1 information  
   
emp1.display();   
  
#accessing display() method to print employee 2 information  
emp2.display(); 

class Student:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
    def display_details(self):  
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))  
s = Student("Mishan",101,22)  
print(s.__doc__)  
print(s.__dict__)  
print(s.__module__) 