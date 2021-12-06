# class Phone:
#     def __init__(self, number1,number2,number3):
#         self.number1=number1
#         self.number2 = number2 
#         self.number3 = number3


#     def TurningOn(self):
#         return " Mobile Phone " + self.number1 + " is turned on  \n   Mobile Phone " + self.number2 + " is turned on"

#     def Calling(self):
#         return "Calling "+ self.number3

#     def TurningOff(self):
#         return "Mobile Phone " + self.number1 + " is turned off  \n   Mobile Phone " + self.number2 + " is turned off"

# Iphone = Phone("22-4444444","997","2535352")
# print(Iphone.TurningOn())
# print(Iphone.Calling())
# print(Iphone.TurningOff())





#TurnOn= Login("mobile phone", + number1 ,"is turned on")

# class Car:
#     def __init__(self, brand,name,color,year):
#         self.brand = brand
#         self.name = name
#         self.color = color
#         self.year = year
#         self.miles = 1
#         self.settopspeed(230)
#         self.printinfo()



#     def printinfo(self):
#         print(self.brand,self.name,self.color,self.year,self.miles,self.topspeed)


#     def settopspeed(self,topspeed):
#         self.topspeed = topspeed
# mustang =Car("Ford","Mustang","red",1970)
# mustang.miles= 100

# mustang.printinfo()


# charger = Car("Dodge", "Charger","Blue",1971)



# class Book:
    
    
#     def __init__(self,author,title="Uknown",isbn="Unknown",year="Unknown"):
#         self.author = author
#         self.title = title #tylko można mieć 1 konstruktor!
#         self.isbn = isbn
#         self.year = year



#     def printdata(self):
#         print(self.author,self.title,self.isbn,self.year)

# book1 =Book("Ola Kowalska", "Podróże","123dczxcxz3",2020)
# book1.printdata()
# book2=Book("ADAM",year = 2010, isbn=300)
# book2.printdata()

# class Laptop:
#     def __init__(self,cpu,ram=4096,gpu="AMD",price=2000):
#         self.setCpu(cpu)
#         self.setram(ram)
#         self.gpu = gpu
#         self.price = price


#     def setCpu(self,cpu):
#         if cpu.lower() == "amd" or cpu.lower() =="intel" or cpu.lower()=="arm":
#             self.cpu =cpu
#         else:
#             self.cpu = "Unknown"

#     def setram(self, ram):
#         print(type(ram))
#         if type(ram) == int and ram >= 2048:
#             self.ram = ram
#         else:
#             self.ram = 2048
    
#     def printdata(self):
#         print(self.cpu, self.ram, self.gpu, self.price)

# laptop1=Laptop("Intel",2100)
# laptop1.printdata()
import random

class Student:
    def __init__(self, name,surname,age,city):
        self.name=name
        self.surname=surname
        self.age=age
        self.city=city
        self.schoolname = None
        self.fieldofstudy = None

    def printinfo(self):
        print(self.name,self.surname,self.age,self.city,self.schoolname,self.fieldofstudy)




class School:
    def __init__(self, name, city):
        self.name = name
        self.city=city
        self.studentslists = []
        self.fieldofstudy=["IT","Math","Robotyka"]
    
    def addStudent(self,student):
        if isinstance(student, Student):
            self.studentslists.append(student)
            student.schoolname=self.name
            student.fieldofstudy= random.choice(self.fieldofstudy)

    def printschoolinfo(self):
        print("School name: ", self.name, "City: ", self.city)
        print("Students: ")
        for el in self.studentslists:
            el.printinfo()


student1 = Student("Kasia","Lis",20,"Krk")
student1.schoolname="Tech school"
student1.country="Poland"
student1.printinfo()
print(student1.country) 

student2 = Student("Adam","kowal",21,"Wawka")




school = School("Techh School", "Waw")
school.addStudent(student1)
school.addStudent(student2)
school.printschoolinfo()



